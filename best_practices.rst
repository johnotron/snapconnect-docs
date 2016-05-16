Best Practices
==============

When writing your *SNAP Connect*-based application there are a few recommended practices.

Hooks
-----

The first recommend practice is to take advantage of the available hooks for controlling which code is executed when
events occur in *SNAP Connect*. The available hooks are listed in the :doc:`api` section, but typically the most
important to remember are :attr:`~snappy.hooks.HOOK_RPC_SENT` and :attr:`~snappy.hooks.HOOK_SNAPCOM_OPENED`.

Just as :attr:`~snappy.hooks.HOOK_RPC_SENT` is important in a SNAPpy script, it is important in *SNAP Connect* applications. This
hook allows your program to know when the system has completed processing a specific outgoing RPC (either unicast,
multicast, or directed multicast), and if it was queued for transmission successfully. Based on this knowledge it might
be appropriate for your application to send another RPC or know that there is room in the queue to send another RPC.
Just as in SNAPpy, the rpc() method (as well as the mcastRpc() and dmcastRpc() methods) returns immediately and
does not mean your RPC has been, or even will be, sent. This hook does not trigger until *SNAP Connect* is done
processing the specified packet (whether that processing was successful or not).

:attr:`~snappy.hooks.HOOK_SNAPCOM_OPENED` informs your application that you have successfully connected to a remote *SNAP Connect*
instance or another *SNAP Connect* instance has connected to you. This is important to know if your application depends
on having connectivity to another instance. If your application is not connected to another *SNAP Connect* instance or a
SNAP bridge node, all of your RPCs will fail because there is no one else to talk to.

Asynchronous Programming
------------------------

*SNAP Connect* is designed to run in a single process within a single thread. As you have seen in our sample
applications, once *SNAP Connect* and your application are initialized, we call *SNAP Connect's*
:meth:`~snapconnect.snap.Snap.loop()` method. This method is a convenience method that is a “while True” loop that
continually calls *SNAP Connect's* :meth:`~snapconnect.snap.Snap.poll()` method:

.. code-block:: python

    def loop(self):
        while True:
            self.poll()
            time.sleep(0.001)

As mentioned in the :doc:`api` section, the :meth:`~snapconnect.snap.Snap.poll()` method calls the necessary
components that *SNAP Connect* uses. Since your program is essentially always running that loop, your application must
be programmed in an asynchronous fashion.

To aid in writing asynchronous programs, access to the asynchronous event scheduler that *SNAP Connect* uses is
available. The event scheduler that *SNAP Connect* uses is part of a Python package called “apy”.

The apy Package
^^^^^^^^^^^^^^^

“apy” is short for “asynchronous Python” and is an open-source pure Python package that comes bundled with *SNAP
Connect*. It is also available from http://sourceforge.net/projects/apy/.

The apy event scheduler is straightforward to use and allows your program to schedule functions to be called. Access
to the event scheduler is available by calling methods on the “scheduler” property of your *SNAP Connect* instance. To
schedule a function to be called later you would call the schedule method. For example, to schedule sending a
multi-cast RPC call every one and a half seconds you could enter:

.. code-block:: python

    def my_func(self):
        self.snap.mcast_rpc(1, 1, "hello")
        return True
    def start_mcasting(self):
        self.snap.scheduler.schedule(1.5, self.my_func)

The signature for the schedule function looks like:

.. function:: schedule(self, delay, callable, *args, **kwargs)

    :param delay: The delay, in seconds, to use before calling the callable argument. A delay of 0 indicates the callable should be called on the next poll interval
    :param callable: The callable object to schedule
    :param \*args: Optional arguments to pass to the callable object
    :param \*\*kwargs: Optional keyword argument to pass to the callable object

The schedule function returns an EventElement object that has a method called “Stop” that enables you to cancel the
scheduled event (in other words, cancel having the callable be called).

For example, to schedule a timeout that can be disabled by calling a specific function you could do:

.. code-block:: python

    def start_timeout(self):
        self.my_timeout = self.snap.scheduler.schedule(10.0, self.on_timeout)

    def disable_timeout(self):
        self.my_timeout.Stop()

The last thing to know about using the apy event scheduler is how to re-schedule a running function after it runs.
When your function returns after being called by the event scheduler, its return value is checked. If the return
value is ``True``, then the event is automatically rescheduled using the original delay value. If you would like to
reschedule with a different delay, your function can return a number (integer or float, indicating a delay duration
in seconds) as a different valid delay value. If you don’t want your function to be rescheduled at all, your function
can return ``None`` or ``False``.

.. code-block:: python

    def reschedule_every_second():
        print 'Tick'
        return 1
    comm.scheduler.schedule(0, reschedule_every_second)

.. code-block:: python

    def reschedule_for_original_delay():
        print 'Tick'
        return True #This will be rescheduled every 5 seconds in this example
    comm.scheduler.schedule(5, reschedule_for_original_delay)

.. code-block:: python

    def do_not_reschedule():
        print 'Tick'
        return False
    comm.scheduler.schedule(5, do_not_reschedule)

Be careful when scheduling *SNAP Connect* functions that have return values. For example, the command:

.. code-block:: python

    comm.scheduler.schedule(0, comm.rpc, addr, "foo")  # <-- DON’T DO THIS!

looks like it would schedule a single RPC call. However, the :meth:`~snapconnect.snap.Snap.rpc` function actually
returns an integer for identifying the packet. This integer will cause the :meth:`~snapconnect.snap.Snap.rpc` function
to be continually rescheduled. Instead, you can use a wrapper that will make the call and return ``None`` to avoid rescheduling.

.. code-block:: python

    def rpc_with_no_return(*args):
        comm.rpc(*args)
        return None
    comm.scheduler.schedule(0, rpc_with_no_return, addr, "foo")


Multiple Instances
------------------
When attempting to run multiple instances of *SNAP Connect* it is important that each instance uses a unique SNAP
address. Just as regular SNAP nodes need a unique address to differentiate each other over the air, *SNAP Connect*
instances need unique addresses on the network as well. A single license file can contain more than one SNAP network
address. When you instantiate your *SNAP Connect* instance you can provide as a keyword argument which SNAP network
address out of the license you would like to use. See the Snap :class:`__init__ <snapconnect.snap.Snap>` fucntion for
more details.