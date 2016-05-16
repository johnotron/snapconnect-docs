==========================
SNAP Connect API Reference
==========================

.. automodule:: snapconnect.snap

Functions
=========

\__init__
---------
.. autoclass:: Snap

accept_sniffer
--------------
.. automethod:: Snap.accept_sniffer

accept_tcp
----------
.. automethod:: Snap.accept_tcp

add_rpc_func
------------
.. automethod:: Snap.add_rpc_func

allow_serial_sharing
--------------------
.. automethod:: Snap.allow_serial_sharing

cancel_upgrade
--------------
.. automethod:: Snap.cancel_upgrade

close_all_serial
----------------
.. automethod:: Snap.close_all_serial

close_serial
------------
.. automethod:: Snap.close_serial

connect_tcp
-----------
.. automethod:: Snap.connect_tcp

data_mode
---------
.. automethod:: Snap.data_mode

directed_mcast_rpc
------------------
.. automethod:: Snap.directed_mcast_rpc

disconnect_tcp
--------------
.. automethod:: Snap.disconnect_tcp

dmcast_rpc
----------
.. automethod:: Snap.dmcast_rpc
.. versionadded:: 3.4

dmcastRpc
---------
.. seealso::
    :meth:`~Snap.dmcast_rpc`

get_info
--------
.. automethod:: Snap.get_info

getInfo
-------
.. seealso::
    :meth:`~Snap.get_info`

load_nv_param
-------------
.. automethod:: Snap.load_nv_param

loadNvParam
-----------
.. seealso::
    :meth:`~Snap.load_nv_param`

local_addr
----------
.. automethod:: Snap.local_addr

localAddr
---------
.. seealso::
    :meth:`~Snap.local_addr`

loop
----
.. automethod:: Snap.loop

mcast_data_mode
---------------
.. automethod:: Snap.mcast_data_mode

mcast_rpc
---------
.. automethod:: Snap.mcast_rpc

mcastRpc
--------
.. seealso::
    :meth:`~Snap.mcast_rpc`

open_serial
-----------
.. automethod:: Snap.open_serial(serial_type, port, reconnect=False, dll_path=MODULE_PATH, forward_groups=None, baudrate=None, io_loop=None)

poll
----
.. automethod:: Snap.poll

poll_internals
--------------
.. automethod:: Snap.poll_internals

replace_rpc_func
----------------
.. automethod:: Snap.replace_rpc_func

rpc
---
.. automethod:: Snap.rpc

rpc_alternate_key_used
----------------------
.. automethod:: Snap.rpc_alternate_key_used

rpc_source_addr
---------------
.. automethod:: Snap.rpc_source_addr

rpcSourceAddr
-------------
.. seealso::
    :meth:`~Snap.rpc_source_addr`

rpc_source_interface
--------------------
.. automethod:: Snap.rpc_source_interface

rpc_use_alternate_key
---------------------
.. automethod:: Snap.rpc_use_alternate_key

save_nv_param
-------------
.. automethod:: Snap.save_nv_param

saveNvParam
-----------
.. seealso::
    :meth:`~Snap.save_nv_param`

set_hook
--------
.. automethod:: Snap.set_hook

setHook
-------
.. seealso::
    :meth:`~Snap.set_hook`

start_sniffer
-------------
.. automethod:: Snap.start_sniffer

stop_accepting_sniffer
----------------------
.. automethod:: Snap.stop_accepting_sniffer

stop_accepting_tcp
------------------
.. automethod:: Snap.stop_accepting_tcp

stop_sniffer
------------
.. automethod:: Snap.stop_sniffer

traceroute
----------
.. automethod:: Snap.traceroute

upgrade_firmware
----------------
.. automethod:: Snap.upgrade_firmware


Constants and Enumerations
==========================

This section lists and describes the numerous constants defined by the SNAP Connect libraries for readability.

.. note::
    Most of these constants are defined by the snap module, and so need a “snap.” prefix on them. For readability within
    this document, the leading “snap.” prefix is not usually shown, however within your code you will need to specify it.

For example:

.. code-block:: python

    save_nv_param( snap.NV_AES128_ENABLE_ID, snap.ENCRYPTION_TYPE_NONE )

Some constants have an additional prefix; for example the various “HOOK_xxx” constants are moved into a “hooks” group.
Those prefixes will be shown in this section, but the leading “snap.” portion must be added too.

For example:

.. code-block:: python

    set_hook(snap.hooks.HOOK_TRACEROUTE, trace_route_handler)

Encryption
----------

+------------------------+---------------------------------------+
| Constant               | Description                           |
+========================+=======================================+
| ENCRYPTION_TYPE_NONE   | Used to turn off encryption.          |
+------------------------+---------------------------------------+
| ENCRYPTION_TYPE_AES128 | Used to enable AES-128 encryption.    |
+------------------------+---------------------------------------+
| ENCRYPTION_TYPE_BASIC  | Used to enable basic SNAP encryption. |
+------------------------+---------------------------------------+

Serial port operations
----------------------

You will use the following constants as the serial_type parameter to the :meth:`close_serial()`, :meth:`open_serial()`,
:attr:`~snappy.hooks.HOOK_SERIAL_OPEN`, and :attr:`~snappy.hooks.HOOK_SERIAL_CLOSE` handler functions.

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Constant                 | Description                                                                                                                                                                                                                                                                                                            |
+==========================+========================================================================================================================================================================================================================================================================================================================+
| SERIAL_TYPE_SNAPSTICK100 | The SN132 SNAPstick, sometimes referred to as a “paddle board”, or the SN163 demonstration board, sometimes referred to as a “bridge board”. These are easily recognized, since they have no case (cover), and you can swap out the SNAP Engine on it for a different model. These have to be plugged into a USB port. |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SERIAL_TYPE_SNAPSTICK200 | The SS200 SNAP Stick, which is much smaller than the SN132, does have a plastic case, and does not accept plug-in SNAP Engines. (It is completely self-contained.) These have to be plugged into a USB port.                                                                                                           |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SERIAL_TYPE_RS232        | “True” COM port, or a USB-serial cable.                                                                                                                                                                                                                                                                                |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Set_hook()
----------

You will use the following constants as the hook parameter to the set_hook() function.

.. seealso::
    * :attr:`~snappy.hooks.HOOK_SNAPCOM_OPENED`
    * :attr:`~snappy.hooks.HOOK_SNAPCOM_CLOSED`
    * :attr:`~snappy.hooks.HOOK_SERIAL_CLOSE`
    * :attr:`~snappy.hooks.HOOK_SERIAL_OPEN`
    * :attr:`~snappy.hooks.HOOK_RPC_SENT`
    * :attr:`~snappy.hooks.HOOK_STDIN`
    * :attr:`~snappy.hooks.HOOK_TRACEROUTE`
    * :attr:`~snappy.hooks.HOOK_OTA_UPGRADE_COMPLETE`
    * :attr:`~snappy.hooks.HOOK_OTA_UPGRADE_STATUS`

Rpc_source_interface()
----------------------

+------------------------+------------------------------------------------------------------------------------------+
| Constant               | Description                                                                              |
+========================+==========================================================================================+
| INTF_TYPE_UNKNOWN      | (you should never see this)                                                              |
+------------------------+------------------------------------------------------------------------------------------+
| INTF_TYPE_802154       | For future use, as SNAP Connect currently relies on a “bridge” node to provide the radio |
+------------------------+------------------------------------------------------------------------------------------+
| INTF_TYPE_SERIAL – RPC | call came in over RS-232                                                                 |
+------------------------+------------------------------------------------------------------------------------------+
| INTF_TYPE_SILABS_USB   | RPC call came in over a Silicon Labs USB interface chip (i.e., an SN132 or SN163)        |
+------------------------+------------------------------------------------------------------------------------------+
| INTF_TYPE_ETH_RPC      | call came in over TCP/IP                                                                 |
+------------------------+------------------------------------------------------------------------------------------+
| INTF_TYPE_SNAPSTICK    | RPC call came in from an SS200 SNAPstick                                                 |
+------------------------+------------------------------------------------------------------------------------------+

SPY Uploading
-------------

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| Constant                      | Description                                                                                                   |
+===============================+===============================================================================================================+
| SNAPPY_PROGRESS_ERASE         | Previous script has been erased                                                                               |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| SNAPPY_PROGRESS_UPLOAD        | “Chunk” of script accepted                                                                                    |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| SNAPPY_PROGRESS_COMPLETE      | Upload completed successfully                                                                                 |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| SNAPPY_PROGRESS_ERROR         | Upload failed                                                                                                 |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| SNAPPY_PROGRESS_TIMEOUT       | Node failed to respond                                                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| SNAPPY_PROGRESS_WRITE_ERROR   | FLASH write failure                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| SNAPPY_PROGRESS_WRITE_REFUSED | Power too low to attempt                                                                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| SNAPPY_PROGRESS_UNSUPPORTED   | Node does not support script upload. For example, it is a SNAP Connect instance rather than an embedded node. |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+

.. _ConstantsUsedWithFirmwareUpgrades:

Firmware upgrades
-----------------

+----------------------------+-----------------------------------------------------+
| Constant                   | Description                                         |
+============================+=====================================================+
| OTA_PROGRESS_COMPLETE      | Upgrade completed successfully                      |
+----------------------------+-----------------------------------------------------+
| OTA_PROGRESS_ERROR         | Upgrade failed                                      |
+----------------------------+-----------------------------------------------------+
| OTA_PROGRESS_CANCELED      | Upgrade canceled                                    |
+----------------------------+-----------------------------------------------------+
| OTA_PROGRESS_TIMEOUT       | Node failed to respond                              |
+----------------------------+-----------------------------------------------------+
| OTA_PROGRESS_WRITE_ERROR   | FLASH write failure                                 |
+----------------------------+-----------------------------------------------------+
| OTA_PROGRESS_WRITE_REFUSED | Power too low to attempt                            |
+----------------------------+-----------------------------------------------------+
| OTA_PROGRESS_UNSUPPORTED   | Node does not support over the air firmware upgrade |
+----------------------------+-----------------------------------------------------+

.. _StringConstantsUsedWithLogging:

Logging
-------

Python logging supports fine grained control of level (verbosity).

The levels that can be applied are DEBUG, INFO, WARNING, ERROR, and FATAL, where DEBUG is the most verbose, and FATAL is the least.

To change the log level globally, you would do something like:

.. code-block:: python

    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

To change the level on a per-module basis, you use the name of the module: “apy”, “SerialWrapper”, “snap”, or “snaplib”. For example:

.. code-block:: python

    snaplib_log = logging.getLogger('snaplib')
    snaplib_log.setLevel(logging.ERROR)

Even finer grained control is possible, but you have to know the name (label) of the loggers you want to control. That is the purpose of this next list.

* “SerialWrapper”

    * “SerialWrapper.pySerialSocket”

* “snap”

    * “snap.AutoSaver”
    * “snap.Deferred”
    * “snap.PacketSink”
    * “snap.dispatchers”
    * “snap.listeners”
    * “snap.mesh”
    * “snap.SNAPtcpConnection”
    * “snap.SNAPtcpServer”

* “snaplib”

    * “snaplib.ComUtils”
    * “snaplib.EventCallbacks”
    * “snaplib.PacketQueue”
    * “snaplib.PacketSerialProtocol”
    * “snaplib.PySerialDriver”
    * “snaplib.RpcCodec”
    * “snaplib.TraceRouteCodec”
    * “snaplib.ScriptsManager”
    * “snaplib.SerialConnectionManager”
    * “snaplib.SnappyUploader”

For example:

.. code-block:: python

    snaplib_log = logging.getLogger('snaplib.RpcCodec')
    snaplib_log.setLevel(logging.INFO)

.. _nv-parameters::

NV Parameters
=============

Embedded SNAP Nodes keep configuration parameters in physical Non-Volatile (NV) memory.

SNAP Connect emulates this type of configuration repository using a standard Python pickle file named ``nvparams.dat``.

The following non-volatile parameters are available through the :meth:`~Snap.save_nv_param()`
and :meth:`~Snap.load_nv_param()` API functions.

.. note::
    Unlike in embedded SNAP nodes, SNAP Connect NV Parameter changes take effect immediately (no reboot required).

Here are all of the System (Reserved) NV Parameters (sorted by numeric ID) that apply to SNAP Connect, and what they
do. You can use these same constants when accessing NV parameters on an embedded node from a SNAP Connect script,
even if the parameter has no meaning in the SNAP Connect context (such as querying for a node’s radio link quality
threshold).

Embedded SNAP Nodes use these same NV parameters, plus many more. Refer to the SNAP Reference Manual for more
information.

You can also define your own NV Parameters (in the range 128-254) which your script can access and modify, just like
the system NV Parameters.

ID 0-4
------
.. autoattribute:: snapconnect.snap.NV_MAC_ADDR_ID

.. autoattribute:: snapconnect.snap.NV_NETWORK_ID

.. autoattribute:: snapconnect.snap.NV_CHANNEL_ID

Reserved for Synapse Use, not used by SNAP Connect

ID 5
----
.. autoattribute:: snapconnect.snap.NV_GROUP_INTEREST_MASK_ID

**Multi-cast Processed Groups**

This is a 16-bit field controlling which multi-cast groups the node will respond to. It is a bit mask, with each bit
representing one of 16 possible multi-cast groups. For example, the 0x0001 bit represents the default group, or
“broadcast group.” (Any node not a member of this group will not respond to route requests, and thus will not
participate in mesh routing for other nodes.)

One way to think of groups is as “logical sub-channels” or as “subnets.” By assigning different nodes to different
groups, you can further subdivide your network.

For example, Portal could multi-cast a “sleep” command to group 0x0002, and only nodes with that bit set in their
Multi-cast Processed Groups field would go to sleep. (This means nodes with their group values set to 0x0002, 0x0003,
0x0006, 0x0007, 0x000A, 0x000B, 0x000E, 0x000F, 0x0012, etc., would respond.) Note that a single node can belong to
any (or even all) of the 16 groups.

Group membership does not affect how a node responds to a direct RPC call. It only affects multi-cast requests.

ID 6
----
.. autoattribute:: snapconnect.snap.NV_GROUP_FORWARDING_MASK_ID

**Multi-cast Forwarded Groups**

This is a separate 16-bit field controlling which multi-cast groups will be re-transmitted (forwarded) by the node.
It is a bit mask, with each bit representing one of 16 possible multi-cast groups. For example, the 0x0001 bit
represents the default group, or “broadcast group.”

By default, all nodes process and forward group 1 (broadcast) packets.

Please note that the Multi-cast Processed Groups and Multi-cast Forwarded Groups fields are independent of each other.
A node could be configured to forward a group, process a group, or both. It can process groups it does not forward,
or vice versa.

.. note::
    Every interface opened in a SNAP Connect application has a forward_groups=None parameter available when you
    open (or listen for) the interface. This parameter restricts which multicast messages will be forwarded through that
    interface from the SNAP Connect instance, with the default value of None indicating that the interface will only
    allow multicast packets for groups that the SNAP Connect instance itself would forward. The hazard here is that if
    you do not explicitly set the forward_groups parameter when you open a connection, SNAP Connect will only be able to
    make multicast requests of nodes in groups that it would normally forward. In other words, if you want SNAP Connect
    to be able to initiate multicast requests to a group that it would not normally forward, you must explicitly set that
    group as a forwarding group when you open the interface.

    If you set your bridge node to not forward multi-cast commands, any Portal or SNAP Connect attached to that
    bridge will not be able to multi-cast to the rest of your network.

ID 7
----
.. autoattribute:: snapconnect.snap.NV_MFG_DATE_ID

Reserved for Synapse Use, not used by SNAP Connect

ID 8
----
.. autoattribute:: snapconnect.snap.NV_DEVICE_NAME_ID

**Device Name**

This NV Parameter lets you choose a name for the node. If this parameter is set to None, then the node name will
default to “SNAPcom”. You do not have to give your nodes explicit names.

.. note::
    It is invalid to put embedded spaces in your Device Name. “My Node” is not a legal name, while “My_Node” is.

ID 9-10
-------
.. autoattribute:: snapconnect.snap.NV_SYSTEM_ERROR_ID

.. autoattribute:: snapconnect.snap.NV_DEVICE_TYPE_ID

Reserved for Synapse Use, not used by SNAP Connect

ID 11
-----
.. autoattribute:: snapconnect.snap.NV_FEATURE_BITS_ID

**Feature Bits**

These control some miscellaneous hardware settings on embedded SNAP Nodes. The only Feature Bits that apply to a SNAP Connect instance are:
    * ``Bit  8 (0b0000,0001,0000,0000 0x0100)`` – Enable second RPC CRC
    * ``Bit 10 (0b0000,0100,0000,0000 0x0400)`` – Enable packet CRC

The second CRC bit (0x100) enables a second CRC packet integrity check on platforms that support it. Setting this bit
tells the SNAP node to send a second cyclical redundancy check (using a different CRC algorithm) on each RPC or
multicast packet, and require this second CRC on any such packet it receives. This reduces the available data
payload by two bytes (to 106 bytes for an RPC message, or 109 bytes for a multicast message), but provides an
additional level of protection against receiving (and potentially acting upon) a corrupted packet. The CRC that has
always been a part of SNAP packets means that there is a one in 65,536 chance that a corrupted packet might get
interpreted as valid. The second CRC should reduce this to a less than a one in four billion chance.

If you set this bit for the second RPC CRC, you must set it in all nodes in your network, and enable the feature in
your Portal preferences or as a feature bit in your SNAP Connect NV parameters.

A node that does not have this parameter set will be able to hear and act on messages from a node that does have it
set, but will not be able to communicate back to that node. Not all platforms support this second CRC. Refer to each
platform’s details in the SNAP Reference Manual to determine whether this capability is available.

The packet CRC bit (0x400) enables SNAP Connect to communicate with a network where packet CRC is enabled. This
applies a second CRC to every packet instead of just RPC (and multicast RPC) packets. Enabling both packet CRC and
second RPC CRC will result in RPC packets using three CRC values when sent over the air.

Unlike the second RPC CRC, the packet CRC is not used over packet serial connections. Packets traveling between the
bridge node and SNAP Connect will not have the extra CRC applied. However, because these packets may end up over the
air, this feature needs to be enabled in SNAP Connect to ensure your packets do not exceed the maximum size when this
feature is enabled.

If you set this bit for the packet CRC, you should set it in all nodes in your network, and enable the feature in
your Portal preferences or as a feature bit in your SNAP Connect NV parameters.

Not all platforms support this packet CRC. Refer to each platform’s details in the SNAP Reference Manual to determine
whether this capability is available.

Binary notations are provided here for clarity. You should specify the parameter value using the appropriate
hexadecimal notation. For example, 0x041F corresponds to 0b0000,0100,0001,1111.

ID 12-18
--------
.. autoattribute:: snapconnect.snap.NV_DEFAULT_UART_ID

.. autoattribute:: snapconnect.snap.NV_UART_DM_TIMEOUT_ID

.. autoattribute:: snapconnect.snap.NV_UART_DM_THRESHOLD_ID

.. autoattribute:: snapconnect.snap.NV_UART_DM_INTERCHAR_ID

.. autoattribute:: snapconnect.snap.NV_CARRIER_SENSE_ID

.. autoattribute:: snapconnect.snap.NV_COLLISION_DETECT_ID

.. autoattribute:: snapconnect.snap.NV_COLLISION_AVOIDANCE_ID

Reserved for Synapse Use, not used by SNAP Connect

ID 19
-----
.. autoattribute:: snapconnect.snap.NV_SNAP_MAX_RETRIES_ID

**Unicast Retries**

This lets you control the number of unicast transmit attempts. This parameter defaults to 8.

This parameter refers to the total number of attempts that will be made to get an acknowledgement back on a unicast
transmission to another node.

In some applications, there are time constraints on the “useful lifetime” of a packet. In other words, if the packet
has not been successfully transferred by a certain point in time, it is no longer useful. In these situations, the
extra retries are not helpful – the application will have already “given up” by the time the packet finally gets
through.

By lowering this value from its default value of 8, you can tell SNAP to “give up” sooner. A value of 0 is treated
the same as a value of 1 – a packet gets at least one chance to be delivered no matter what.

If your connection link quality is low and it is important that every packet get through, a higher value here may
help. However it may be appropriate to reevaluate your network setup to determine if it would be better to change the
number of nodes in your network to either add more nodes to the mesh to forward requests, or reduce the number of
nodes broadcasting to cut down on packet collisions.

ID 20
-----
.. autoattribute:: snapconnect.snap.NV_MESH_ROUTE_AGE_MAX_TIMEOUT_ID

**Mesh Routing Maximum Timeout**

This indicates the maximum time (in milliseconds) a route can “live.” This defaults to 0xEA60 (60,000), or one minute.

Discovered mesh routes timeout after a configurable period of inactivity (see #23), but this timeout sets an upper
limit on how long a route will be used, even if it is being used heavily. By forcing routes to be rediscovered
periodically, the nodes will have an opportunity to discover a more efficient route if one becomes available..

Note that you can set this timeout to zero (which will disable it) if you know for certain that your nodes are
stationary, or have some other reason for needing to avoid periodic route re-discovery.

You can use get_info(15) to determine the number of currently active (not timed out) routes.

ID 21
-----
.. autoattribute:: snapconnect.snap.NV_MESH_ROUTE_AGE_MIN_TIMEOUT_ID

**Mesh Routing Minimum Timeout**

This is the minimum time (in milliseconds) a route will be kept. This defaults to 1000, or one second. Note that in a
busy mesh environment, routes may fall out of the route table before this time period has elapsed if the route table
becomes full and another route is discovered.

ID 22
-----
.. autoattribute:: snapconnect.snap.NV_MESH_ROUTE_NEW_TIMEOUT_ID

**Mesh Routing New Timeout**

This is the grace period (in milliseconds) that a newly discovered route will be kept, even if it is never actually
used. This defaults to 5000, or five seconds.

ID 23
-----
.. autoattribute:: snapconnect.snap.NV_MESH_ROUTE_USED_TIMEOUT_ID

**Mesh Routing Used Timeout**

This is how many additional milliseconds of “life” a route gets whenever it is used. This defaults to 5000, or five
seconds.

Every time a known route gets used, its timeout gets reset to this parameter. This prevents active routes from timing
out as often, but allows inactive routes to go away sooner. ``NV_MESH_ROUTE_AGE_MAX_TIMEOUT_ID`` takes precedence
over this timeout.

ID 24
-----
.. autoattribute:: snapconnect.snap.NV_MESH_ROUTE_DELETE_TIMEOUT_ID

**Mesh Routing Delete Timeout**

This timeout (in milliseconds) controls how long “expired” routes are kept around for bookkeeping purposes. This
defaults to 10000, or 10 seconds.

ID 25
-----
.. autoattribute:: snapconnect.snap.NV_MESH_RREQ_TRIES_ID

**Mesh Routing RREQ Retries**

This parameter controls the total number of retries that will be made when attempting to “discover” a route (a
multi-hop path) over the mesh. This defaults to 3.

ID 26
-----
.. autoattribute:: snapconnect.snap.NV_MESH_RREQ_WAIT_TIME_ID

**Mesh Routing RREQ Wait Time**

This parameter (in milliseconds) controls how long a node will wait for a response to a Route Request (RREQ) before
trying again. This defaults to 500, or a half second.

Not that subsequent retries use longer and longer timeouts (the timeout is doubled each time). This allows nodes from
further and further away time to respond to the RREQ packet.

ID 27
-----
.. autoattribute:: snapconnect.snap.NV_MESH_INITIAL_HOPLIMIT_ID

**Mesh Routing Initial Hop Limit**

This parameter controls how far the initial “discovery broadcast” message is propagated across the mesh.

If your nodes are geographically distributed such that they are always more than 1 hop away from their logical peers,
then you can increase this parameter. Consequently, if most of your nodes are within direct radio range of each
other, having this parameter at the default setting of 2 will use less radio bandwidth.

SNAP Connect does not support disabling mesh discovery by setting this value to 0. A value of 0 will be treated as if
you had set the initial hop limit to the default value of 2.

This parameter should remain less than or equal to the next parameter, Mesh Routing Maximum Hop Limit.

ID 28
-----
.. autoattribute:: snapconnect.snap.NV_MESH_MAX_HOPLIMIT_ID

**Mesh Routing Maximum Hop Limit**

To cut down on needless broadcast traffic during mesh networking operation (thus saving both power and bandwidth),
you can choose to lower this value to the maximum number of physical hops across your network. The default value is 5.

.. note:: if your network is larger than 5 hops, you will need to raise this parameter.

ID 29
-----
.. autoattribute:: snapconnect.snap.NV_MESH_SEQUENCE_NUMBER_ID

**Mesh Sequence Number**

Reserved for Synapse Use, not used by SNAP Connect

ID 30
-----
.. autoattribute:: snapconnect.snap.NV_MESH_OVERRIDE_ID

**Mesh Override**

This is used to limit a node’s level of participation within the mesh network.

When set to the default value of 0, the node will fully participate in the mesh networking. This means that not only
will it make use of mesh routing, but it will also “volunteer” to route packets for other nodes.

Setting this value to 1 will cause the node to stop volunteering to route packets for other nodes. It will still
freely use the entire mesh for its own purposes (subject to other nodes’ willingness to route packets for it).

This feature was added to better support nodes that spend most of their time “sleeping.” If a node is likely to spend
most of its time asleep, there may be no point in it becoming part of routes for other nodes while it is (briefly)
awake.

This can also be useful if some nodes are externally powered, while others are battery-powered. Assuming sufficient
radio coverage (all the externally powered nodes can “hear” all of the other nodes), then the Mesh Override can be
set to 1 in the battery powered nodes, extending their battery life at the expense of reducing the “redundancy” in
the overall mesh network.

.. note::Enabling this feature on your bridge node means Portal will no longer be able to communicate with the rest
  of your network, regardless of how everything else is configured. No nodes in your network (except for your bridge
  node) will be able to receive commands or information from Portal or send commands or information to Portal.

ID 31-49
--------
.. autoattribute:: snapconnect.snap.NV_MESH_PENALTY_LQ_THRESHOLD_ID

.. autoattribute:: snapconnect.snap.NV_MESH_REJECTION_LQ_THRESHOLD_ID

.. autoattribute:: snapconnect.snap.NV_CS_CD_LEVEL_ID

.. autoattribute:: snapconnect.snap.NV_SNAP_LQ_THRESHOLD_ID

.. autoattribute:: snapconnect.snap.NV_SNAPPY_CRC_ID

.. autoattribute:: snapconnect.snap.NV_SYS_PLATFORM_ID

Reserved for Synapse Use, not used by SNAP Connect

ID 50
-----
.. autoattribute:: snapconnect.snap.NV_AES128_ENABLE_ID

**Enable Encryption**

Control whether encryption is enabled, and what type of encryption is in use for firmware that supports multiple forms.
The options for this field are:
0 =	Use no encryption. (This is the default setting.)
1 = Use AES-128 encryption if supported.
2 = Use Basic encryption.

If you set this to a value that indicates encryption should be used, but either an invalid encryption key is
specified (in NV Parameter #51), or your Python environment does not support the encryption mode specified, your
transmissions will not be encrypted.

SNAP versions before 2.4 did not include the option for Basic encryption, and nodes upgraded from those firmware
versions may contain False or True for this parameter. Those values correspond to 0 and 1 and will continue to
function correctly. Basic encryption is not as secure as AES-128 encryption, but it is available in all nodes
starting with release 2.4.

If encryption is enabled and a valid encryption key is specified, all communication from the node will be encrypted,
whether it is sent over the air or over a serial connection. Likewise, the node will expect that all communication to
it is encrypted, and will be unable to respond to unencrypted requests from other nodes. If you have a node that you
cannot contact because of a forgotten encryption key, you will have to reset the factory parameters on the node to
reestablish contact with it.

Enabling AES-128 encryption in SNAP Connect requires that you have the third-party PyCrypto Python library installed.
You can acquire the library from http://pycrypto.org/

ID 51
-----
.. autoattribute:: snapconnect.snap.NV_AES128_KEY_ID

**Encryption Key**

The encryption key used by either AES-128 encryption or Basic encryption, if enabled. This NV Parameter is a string
with default value of “”. If you are enabling encryption, you must specify an encryption key. Your encryption key
should be complex and difficult to guess, and it should avoid repeated characters when possible.

An encryption key must be exactly 16 bytes (128 bits) long to be valid. This parameter has no effect unless NV
parameter #50 is also set to enable encryption.

If NV parameter #50 is set for AES-128 encryption and parameter 51 has a valid encryption key, SNAP Connect will fail
with an exception if you do not have the PyCrypto Python library installed.

ID 52
-----
.. autoattribute:: snapconnect.snap.NV_LOCKDOWN_FLAGS_ID

**Lockdown**

If this parameter is 0 (or never set at all), access is unrestricted. You can freely change NV Parameters (even
remotely).

If you set this parameter to 2, then the system enters a “lockdown” mode where remote NV Parameter changes are
disallowed.

Values other than 0 or 2 are reserved for future use, and should not be used on a SNAP Connect node. (The value 1 is
valid on embedded nodes, preventing over-the-air changes to the node’s SNAPpy script.)

ID 53-54
--------
.. autoattribute:: snapconnect.snap.NV_MAX_LOYALTY_ID

Reserved for Synapse Use, not used by SNAP Connect

ID 55
-----
.. autoattribute:: snapconnect.snap.NV_ALTERNATE_KEY_ID

**Alternate Encryption Key** (SNAP Connect only)

This NV parameter is like NV #51 in form and function. It represents a second (“alternate”) encryption key that can be
used in special circumstances.

For example, you could be running a fully encrypted network using key “encryption_key_1” when a new node is added with
encryption key “KEY2(ENCRYPTION)”. By saving the second key in NV #55, and proper use of the add_rpc_func(),
rpc_use_alternate_key(), and rpc_alternate_key_used() functions you can perform multicast interactions with the new
node, while still continuing to interact fully (both multicast and unicast) with the old nodes. This gives you a way to
reprogram the new node to switch over to using the first key without having to pause communications to the rest of
the network.

ID 56-127
---------
.. autoattribute:: snapconnect.snap.NV_LAST_VERSION_BOOTED_ID

.. autoattribute:: snapconnect.snap.NV_REBOOTS_REMAINING_ID

.. autoattribute:: snapconnect.snap.NV_ALT_RADIO_TRIM_ID

.. autoattribute:: snapconnect.snap.NV_VENDOR_SETTINGS_ID

.. autoattribute:: snapconnect.snap.NV_CLOCK_REGULATOR_ID

.. autoattribute:: snapconnect.snap.NV_RADIO_CALIBRATION_ID

.. autoattribute:: snapconnect.snap.NV_TX_POWER_LIMIT_ID

Reserved for Synapse Use, not used by SNAP Connect

ID 128-254
----------
**Available for User Definition**

These are user-defined NV Parameters, and can be used for whatever purpose you choose, just as with embedded SNAP
Nodes. Unlike embedded SNAP nodes, however, SNAP Connect lets you store any pickleable object in an NV parameter,
rather than just a string, Boolean, integer, or None.

ID 255
------
Reserved for Synapse Use, not used by SNAP Connect

.. _authentication-realms:

Authentication Realms
=====================

The realm parameter is used by SNAP Connect when forming TCP connections.  The value is passed to the authentication
functions for accepting and connecting TCP.  In versions of SNAP Connect prior to 3.2, this field would always take
on the value “SNAPcom.”  With the addition of remote sniffers in SNAP Connect 3.2, the realm value can now be used to
distinguish between regular TCP connections and remote sniffer TCP connections.

If desired, the realm parameter may be ignored in your client and server authentication functions and the login
information for all connection types will be shared.

REALM_SNAP
----------
.. autoattribute:: snapconnect.snap.REALM_SNAP
    :annotation:

**Standard SNAP over TCP Connections**

This realm will be passed to authentication functions when :meth:`~Snap.connect_tcp()` is used to create a
connection between SNAP Connect instances.  The parameter ``sniffer_callback`` should be set to None when creating a
standard TCP connection.

.. seealso::
    * :meth:`~Snap.accept_tcp()`
    * :meth:`~Snap.connect_tcp()`

REALM_SNIFFER
-------------
.. autoattribute:: snapconnect.snap.REALM_SNIFFER
    :annotation:

**Remote Sniffer connection over TCP**

This realm will be passed to authentication functions when :meth:`~Snap.connect_tcp()` is used to
create a remote sniffer connection between SNAP Connect instances.  The parameter ``sniffer_callback`` should be set
to a callable function when creating a remote sniffer TCP connection.

This realm will only be used if :meth:`~Snap.accept_sniffer()` has been called in addition to
:meth:`~Snap.accept_tcp()`.

.. seealso::
    * :meth:`~Snap.accept_tcp()`
    * :meth:`~Snap.accept_sniffer()`
    * :meth:`~Snap.connect_tcp()`

.. _hooks:

Hooks
=====

SNAP Hooks are events that can occur at runtime. This section lists the supported hooks, their meanings, their
triggers, and their (callback) parameters.

Refer also to the description of the :meth:`~Snap.set_hook()` function earlier in this manual.

HOOK_SNAPCOM_OPENED
-------------------

.. autoattribute:: snappy.hooks.HOOK_SNAPCOM_OPENED
    :annotation:

SNAP COMmunications have been established over a TCP/IP link.

*Triggered by*

Establishment of an inbound or outbound TCP/IP connection with another instance of SNAP Connect (possibly embedded
inside of another application like Portal).

This means the root cause of the ``HOOK_SNAPCOM_OPENED`` was either:
    * a call to :meth:`~Snap.accept_tcp()` that allowed/enabled incoming TCP/IP connections; or
    * a call to :meth:`~Snap.connect_tcp()` that created an outgoing TCP/IP connection.

*Required callback signature*

.. function:: some_function(connection_info, snap_address)

    :param tuple connection_info: (IP address of the other SNAP Connect instance, TCP/IP port of the connection)
    :param string snap_address: this is a Python string containing the three-byte SNAP Address of the other node.

.. note:: If you want to know your own SNAP Address, try the :meth:`~Snap.local_addr()` function.

HOOK_SNAPCOM_CLOSED
-------------------

.. autoattribute:: snappy.hooks.HOOK_SNAPCOM_CLOSED
    :annotation:

SNAP COMmunications have ended (or failed to ever get established) over a TCP/IP link.

*Triggered by*

Shutdown of an established TCP/IP connection, or failure to establish a connection in the first place (for example,
calling :meth:`~Snap.connect_tcp()` with the IP address of a computer that is not running SNAP Connect).

*Required callback signature*

Scenario 1 – connection could not be established

.. py:function:: some_function(connection_info, snap_address)

        :param tuple connection_info: (IP address of the other computer, TCP/IP port of the initial connection attempt)
        :param snap_address: in this scenario, snap_address is None because there was no SNAP Node at the other end of the attempted connection.

Scenario 2 – an established connection was later shut down

.. py:function:: some_function(connection_info, snap_address)

    :param tuple connection_info: (IP address of the other SNAP Connect instance, TCP/IP port of the connection)
    :param string snap_address: this is a Python string containing the three-byte SNAP Address of the other node

In other words, the parameters for a valid connection closing are the same as those when it was initially opened. (See :attr:`~snappy.hooks.HOOK_SERIAL_OPEN`).

HOOK_SERIAL_OPEN
----------------

.. autoattribute:: snappy.hooks.HOOK_SERIAL_OPEN
    :annotation:

Communications over a specific serial (USB or RS-232) interface have started.

*Triggered by*

This event will occur after every successful call to :meth:`~Snap.open_serial()`.  After
:meth:`~Snap.open_serial()` is called, SNAP Connect will attempt to retrieve the address of the device
attached to the serial port.  This event will trigger after the address has been retrieved or the retrieval attempt has
timed out.

Because the serial connection is open immediately after the call to :meth:`~Snap.open_serial()`, it is
possible that packets may be received on the interface before the node address can be determined and the hook function
is called.

*Required callback signature*

.. py:function:: some_function(serial_type, port, addr)

    :param serial_type: The type of the serial port, one of: ``SERIAL_TYPE_RS232``, ``SERIAL_TYPE_SNAPSTICK100``, ``SERIAL_TYPE_SNAPSTICK200``
    :param port: The port of that particular type that opened, as appropriate for your operating system. On Windows, port is a zero-based list. (Specify 0 for COM1 for example.) On Linux, port will typically be a string, for example "/dev/ttys1 ".
    :param addr: The address of the SNAP device attached to this serial port, or None if the address could not be retrieved for any reason.

.. note:: These parameters are the same ones used in the initial :meth:`~Snap.open_serial()` call, and in any subsequent :meth:`~Snap.close_serial()` call.

HOOK_SERIAL_CLOSE
-----------------

.. autoattribute:: snappy.hooks.HOOK_SERIAL_CLOSE
    :annotation:

Communications over a specific serial (USB or RS-232) interface have ended.

*Triggered by*

A ``HOOK_SERIAL_CLOSE`` event can be triggered by a call to :meth:`~Snap.close_serial()`, or (in the
case of some removable USB devices) by the physical removal of the device from the computer SNAP Connect is running on.

This event can only occur after a successful call to :meth:`~Snap.open_serial()`.

*Required callback signature*

.. py:function:: some_function(serial_type, port)

    :param serial_type: The type of the serial port, one of: ``SERIAL_TYPE_RS232``, ``SERIAL_TYPE_SNAPSTICK100``, ``SERIAL_TYPE_SNAPSTICK200``
    :param port: The port of that particular type that closed, as appropriate for your operating system. On Windows, port is a zero-based list. (Specify 0 for COM1 for example.). On Linux, port will typically be a string, for example "/dev/ttys1 ".

.. note:: These parameters are the same ones used in the initial :meth:`~Snap.open_serial()` call,
  and in any subsequent :meth:`~Snap.close_serial()` call.

HOOK_RPC_SENT
-------------

.. autoattribute:: snappy.hooks.HOOK_RPC_SENT
    :annotation:

A packet created previously by a call to :meth:`~Snap.rpc()`,
:meth:`~Snap.mcast_rpc()`, or :meth:`~Snap.dmcast_rpc()` has been sent, or given up on
(all retries were exhausted while attempting to send the packet).

*Triggered by*

This event fires after any RPC packet is sent, regardless of whether it was sent by your application code, or
automatically by SNAP Connect behind the scenes.

*Required callback signature*

.. py:function:: some_function(packet_identifier, transmit_success)

    :param packet_identifier: The identifier for which packet was sent.
    :param transmit_success: True if SNAP Connect believes the packet has been transmitted successfully or False if SNAP Connect was unable to send the packet. A successful transmit does not indicate that the packet was able to reach the destination.

.. note:: ``packet_identifier`` is the same identifier that was originally returned by the call to
  :meth:`~Snap.rpc()`, :meth:`~Snap.mcast_rpc()`, or
  :meth:`~Snap.dmcast_rpc()`. For compatibility with embedded SNAP nodes, you can also recover this
  identifier immediately after sending an RPC using get_info(9).

.. note:: Receipt of a ``HOOK_RPC_SENT`` does not mean the packet made it all the way to the other node. This is not an
  end-to-end acknowledgement!  If transmit_success is False, the packet has not been transmitted; but if it is True, that
  is no guarantee the destination node networked through the interface actually received the packet.

SNAP has no provisions for end-to-end acknowledgement at the protocol layer. Any such functionality must be
implemented in your application. For example, have a node send a return RPC in response to a request RPC. Only when
the originating node receives the response RPC can it be certain that the original request made it through.

HOOK_STDIN
----------

.. autoattribute:: snappy.hooks.HOOK_STDIN
    :annotation:

A packet containing user data has been received. This could either be unicast data addressed specifically to this node, or it could be multicast data sent to any nodes within specified multicast group[s].

*Triggered by*

This event is ultimately triggered by some other node invoking :meth:`~Snap.data_mode()` or
:meth:`~Snap.mcast_data_mode()`, if it is a SNAP Connect application.

Alternatively, an embedded SNAP Node (such as an RF100) could be forwarding data (from a serial port for example) by
use of the ``ucastSerial()`` or ``mcastSerial()`` functions (refer to the SNAP Reference Manual).

*Required callback signature*

.. py:function:: some_function(data)

    :param data: The actual data (payload) of the DATA MODE packet.

.. note:: If you need to know who the data came from, try the :meth:`~Snap.rpc_source_addr()` function.

HOOK_TRACEROUTE
---------------

.. autoattribute:: snappy.hooks.HOOK_TRACEROUTE
    :annotation:

A Trace Route has been successfully completed.

*Triggered by*

This event is by invoking the :meth:`~Snap.traceroute()` function for a node that actually is reachable and that can respond.

*Required callback signature*

.. py:function:: some_function(node_addr, round_trip_time, hops)

    :param node_addr: A Python string containing the three-byte SNAP Address of the node that was “traced”.
    :param round_trip_time: the round trip time for the trace route packet, after it made it past the initial hop.
    :param hops: This is a Python list of tuples, with one list entry for every “hop” that the trace route made on its journey to and from the target node.

.. note:: The first hop is not counted in Trace Routes because when the feature was originally implemented it was decided
  to only track the over-the-air timing. Bottom line – the bridge node component of your round_trip_time will be reported
  as 0 milliseconds. For TCP connections, this could significantly under-report the speed of that first hop.

For example, a Trace Route to your directly connected bridge node will have two hops – one for the hop from SNAP
Connect to the bridge node, and a second hop back from the bridge node to SNAP Connect.

Each Python tuple within the hops list will be made up of two values:
    * hop[0] will be the SNAP Address that the Trace Route packet was received from.
    * hop[1] will be the Link Quality at which the Trace Route was received, *if* it was received over a radio link. (Serial links and TCP/IP links have no true “link quality” in SNAP, and will always be reported as having a LQ of 0.) The link quality is reported in (negative) dBm, so lower values represent stronger signals. The theoretical range for the link quality is 0-127.

For an example of how Trace Route results can be displayed, refer to the Portal user interface.

HOOK_OTA_UPGRADE_COMPLETE
-------------------------

.. autoattribute:: snappy.hooks.HOOK_OTA_UPGRADE_COMPLETE
    :annotation:

An over-the-air firmware upgrade has completed.

*Triggered by*

This event follows a call to the :meth:`~Snap.upgrade_firmware()` function.  The event is triggered
when an upgrade completes successfully or an error occurs that halts the upgrades progress.

*Required callback signature*

.. py:function:: some_function(upgrade_addr, status_code, message)

    :param upgrade_addr: The address of the node for which the upgrade has completed.
    :param status_code: The result of the upgrade. See the :ref:`ConstantsUsedWithFirmwareUpgrades` section for more details.
    :param message: A human-readable string describing the cause of an error, or None if the upgrade was successful.

HOOK_OTA_UPGRADE_STATUS
-----------------------

.. autoattribute:: snappy.hooks.HOOK_OTA_UPGRADE_STATUS
    :annotation:

An over-the-air firmware upgrade status has advanced.

*Triggered by*

This event follows a call to the :meth:`~Snap.upgrade_firmware()` function.  The event is triggered
every time progress is made in an over the air upgrade and will be called many times for every upgrade started and not
immediately stopped.

*Required callback signature*

.. py:function:: some_function(upgrade_addr, percent_complete)

    :param upgrade_addr: The address of the node receiving the upgrade.
    :param percent_complete: An estimate (as a Python float) of how much of an upgrade has been completed, as a percentage.

.. note::
    To determine when an upgrade is entirely complete see the :attr:`~snappy.hooks.HOOK_OTA_UPGRADE_COMPLETE` section.

.. _exceptions:

Exceptions
==========

When invoking SNAP Connect functions, your program should be prepared to “catch” any Python exceptions that are “thrown” (raised).

The following lists the possible Python exceptions that can be thrown by the SNAP Connect libraries, and some possible causes (exception text messages).

.. note:: Obvious exceptions like Exception, KeyboardInterrupt, and SystemExit are not shown.

Exceptions that can be thrown from the ``apy`` package
------------------------------------------------------

The monotime module in the apy package can throw the following exception:
    * :exc:`OSError`

The PostThread module in the apy package can throw the following exception:
    * :exc:`RuntimeError`

Exceptions that can be thrown from the ``serialwrapper`` package
----------------------------------------------------------------

The ``ComUtil`` module in the ``serialwrapper`` package can throw the following exceptions:
    * :exc:`NoMorePortsError`
        * “No more ports to scan”
    * :exc:`Exception`
        * “Did not receive expected response”
        * “Unknown probe version”

The ``ftd2xxserialutil`` module in the ``serialwrapper`` package can throw the following exceptions:
    * :exc:`Ftd2xxSerialException`
        * “Cannot set number of devices”
    * :exc:`ValueError`
        * “Serial port MUST have enabled timeout for this function!”
        * “Not a valid port: ...”
        * “Not a valid baudrate: ...”
        * “Not a valid byte size: ...”
        * “Not a valid parity: ...”
        * “Not a valid stopbit size: ...”
        * “Not a valid timeout: ...”

The ``ftd2xxserialwin32`` module in the ``serialwrapper`` package can throw the following exceptions:
    * :exc:`Ftd2xxSerialException`
        * “Port must be configured before it can be used”
        * “Could not find devices to open: …”
        * “Could not find port: …”
        * “Could not open device: …”
        * “Could not set latency: …”
        * “Can only operate on an open port”
        * “Could not set timeouts: …”
        * “Could not set baudrate: …”
        * “Could not set break: …”
        * “Could not reset break: …”
        * “Could not get CTS state: …”
        * “Could not get DSR state: …”
        * “Could not get RI state: …”
        * “Could not get DCD state: …”
        * “Could not set stopbits, parity, and/or bits per word: …”
        * “Could not set flow control: …”
        * “Cannot configure port, some setting was wrong…”
        * “An error occurred while checking rx queue: …”
        * “An error occurred while reading: …”
        * “An error occurred while writing: …”
        * “An error occurred while flushing the input buffer: …”
        * “An error occurred while setting RTS: …”
        * “An error occurred while clearing RTS: …”

The ``PyserialDriver`` module in the ``serialwrapper`` package can throw the following exceptions:
    * :exc:`Exception`
        * “Buffers don’t match”
    * :exc:`Serial.SerialException`
        * “WriteFile failed…”
        * “write failed: ...”
    * :exc:`PortNotOpenError`
    * :exc:`TypeError`
        * “Expected str or bytearray, got ...”
        * “Unknown serial driver type”
        * “Unsupported output type”
    * :exc:`SerialOpenException`
        * “SNAP USB devices are not currently supported on this platform”
        * “An error occurred while setting up the serial port: …”

The ``usbxserialutil`` module in the ``serialwrapper`` package can throw the following exceptions:
    * :exc:`ValueError`
        * “Serial port MUST have enabled timeout for this function!”
        * “Not a valid port: …”
        * “Not a valid baudrate: …”
        * “Not a valid byte size: …”
        * “Not a valid parity: …”
        * “Not a valid stopbit size: …”
        * “Not a valid timeout: …”
    * :exc:`UsbxSerialException`
        * “Cannot set number of devices”

The ``usbxserialwin32`` module in the ``serialwrapper`` package can throw the following exceptions:
    * :exc:`portNotOpenError`
    * :exc:`UsbxSerialException`
        * “Port must be configured before it can be used”
        * “Unable to verify device PID: …”
        * “USB device was not found to be a SNAP USB device”
        * “Could not open device: …”
        * “Can only operate on an open port”
        * “Could not set timeouts: …”
        * “Could not set baud rate: …”
        * “Could not set stop bits, parity, and/or bits per word: …”
        * “Could not set flow control: …”
        * “Cannot configure port, some setting was wrong: …”
        * “Could not get CTS state…”
        * “An error occurred while checking rx queue: …”
        * “An error occurred while reading: …”
        * “Write time out occurred and there are no USB devices”
        * “A system error occurred while writing: …”
        * “An error occurred while flushing the input buffer: …”
        * “An error occurred while flushing the output buffer: …”

Exceptions that can be thrown from the ``snapconnect`` package
--------------------------------------------------------------

The ``auth_digest`` module in the ``snapconnect`` package can throw the following exceptions:
    * :exc:`cherrypy.HTTPError`
        * “Bad Request…”
        * “You are not authorized to access that resource”
    * :exc:`ValueError`
        * “Authorization scheme is not Digest”
        * “Unsupported value for algorithm…”
        * “Not all required parameters are present”
        * “Unsupported value for qop: …”
        * “If qop is sent then cnonce and nc MUST be present”
        * “If qop is not sent, neither cnonce nor nc can be present”
        * “Unrecognized value for qop: …”

The ``dispatchers`` module in the ``snapconnect`` package can throw the following exception:
    * :exc:`TypeError`
        * “Unknown descriptor type”

The ``LicenseManager`` module in the ``snapconnect`` package can throw the following exception:
    * :exc:`LicenseError`
        * “… license file has expired”
        * “Your license is invalid…”
        * “Unable to load license file…”

The ``listeners`` module in the ``snapconnect`` package can throw the following exception:
    * :exc:`ValueError`
        * “Unknown serial type”

The ``snap`` module in the ``snapconnect`` package can throw the following exceptions:
    * :exc:`ImportError`
        * “Unable to find PyCrypto library required for AES support”
    * :exc:`IOError`
        * “Unable to load NV params file: …”
    * :exc:`RuntimeError`
        * “Non-licensed address provided”
        * “Invalid license found”
        * “Unable to determine callable functions”
        * “Tornado ioloop not supported”
        * “You must be accepting TCP connections to call accept_sniffer()”
    * :exc:`TypeError`
        * “Unknown Hook Type”
        * “Invalid callback”
        * “Invalid connection parameter provided”
    * :exc:`ValueError`
        * “Unknown encryption type specified: …”
        * “auth_info is not callable”
        * “Serial interface type must be an integer”
        * “Unsupported serial interface type”

The ``snaptcp`` module in the ``snapconnect`` package can throw the following exceptions:
    * :exc:`socket.error`
        * “Did not receive a valid lookup result”
    * :exc:`ValueError`
        * “SSL support was not found”

Exceptions that can be thrown from the ``snaplib`` package
----------------------------------------------------------
The ``DataModeCodec`` module in the ``snaplib`` package can throw the following exception:
    * :exc:`DataModeEncodeError`
        * “Packet is greater than 255 bytes”
        * “The packet is too large to encode …”

The ``MeshCodec`` module in the ``snaplib`` package can throw the following exception:
    * :exc:`MeshError`
        * “encode function does not yet support message type …”
        * “Packet is greater than 255 bytes”
        * “Mesh Routing message too large to encode …”

The ``RpcCodec`` module in the ``snaplib`` package can throw the following exceptions:
    * :exc:`RpcError`
        * “Do not receive a list of arguments”
        * “Source Address must be 3 bytes”
        * “Source Address must be between \xFF\xFF\xFF and \x00\x00\x00”
        * “No source address was set”
        * “No destination address/group was set”
        * “dmcast_dstAddrs length must be a multiple of 3 (including 0)”
        * “Original TTL for multicast must be greater than 0 and less than 256”
        * “Delay Factor for directed multicast must be between 0 and 255”
        * “The multicast group must be 2 bytes”
        * “Destination multicast group cannot be all zeros”
        * “TTL for multicast must be greater than 0 and less than 256”
        * “Packet cannot be a Directed Multicast without being a Multicast Packet first”
        * “The destination address must be 3 bytes”
        * “Int out of range”
        * “Function name cannot be None”
        * “Max string length is 255”
        * “Unsupported DataType: …”
        * “Packet is greater than 255 bytes”
        * “Function/Args too large to encode …”
    * :exc:`TypeError`
        * “Unsupported type …”
        * “String length is greater than 255”
        * “Integer is out of range”
    * :exc:`WrongArgCount`

The ``SnappyUploader`` module in the ``snaplib`` package can throw the following exception:
    * :exc:`AlreadyInProgressError`
        * “There is currently a SNAPpy upload already in progress”

The ``TraceRouteCodec`` module in the ``snaplib`` package can throw the following exception:
    * :exc:`TraceRouteEncodeError`
        * “The data is too large to encode”
        * “Packet is greater than 255 bytes”

.. _sniffer-descriptors:

Sniffer Descriptors
===================

SNAP Descriptors are objects that are passed to local and remote sniffer callbacks.  These descriptors represent packets
that are received and transmitted by a SNAP Connect instance.  This section lists the supported descriptors, their
meanings, and their attributes.

The descriptors passed to sniffer functions are NOT over-the-air packets. These descriptors only represent packets that
are received and transmitted over SNAP Connect serial and TCP connections.

Refer also to the description of the :meth:`~Snap.accept_sniffer()`,
:meth:`~Snap.connect_tcp()`, and :meth:`~Snap.start_sniffer()` functions earlier in this
manual.

.. note:: Because not every descriptor type supports every attribute, you will want to use the Python builtin function ``isinstance(descriptor, descriptor_type)`` to verify the descriptor type prior to accessing its attributes.

All packet descriptors share several attributes in common:
    * ``raw`` : A string of decrypted bytes representing the undecoded packet.
    * ``rx`` : True if the packet was received by the SNAP Connect instance running the sniffer.
    * ``tx`` : True if the packet was transmitted by the SNAP Connect instance running the sniffer.

Data Mode Packets
-----------------

.. attribute:: ``snap.DataModeDescriptor``

``DataModeDescriptor`` represents received and transmitted (originated or forwarded) data mode packets.

See functions :meth:`~Snap.data_mode()` and :meth:`~Snap.mcast_data_mode()`.

See :attr:`~snappy.hooks.HOOK_STDIN` for how data mode packets are normally received.
    * ``data`` : The data being carried by the packet.
    * ``dstAddr`` : A three-byte string representing the immediate destination of the packet (subject to mesh routing) or a two-byte multicast group (for a multicast data mode packet).
    * ``final_dst_addr`` : A three-byte string representing the final destination of the packet (unicast only).
    * ``isMulticast`` : True if the packet is multicast or False if it is unicast.
    * ``seq`` : The sequence number of the packet.
    * ``srcAddr`` : A three-byte string representing the SNAP address of the original source of the packet.
    * ``Ttl`` : The number of hops remaining for this packet (multicast only).

Mesh Routing Packets
--------------------

.. attribute:: ``snap.MeshDescriptor``

``MeshDescriptor`` represents received and transmitted mesh routing packets.
    * ``additionalAddresses`` : An optional list of additional discovered/errored addresses.
    * ``hopLimit`` : The number of hops remaining for this packet.
    * ``msgId`` : A single character representing the type of mesh packet. ‘Q’ is used for route requests, ‘P’ is used for route replies, and ‘E’ is used for route errors.
    * ``source`` : A three-byte string representing the immediate source of the packet.
    * ``originator`` : A three-byte string representing the address of the node that created the packet.
    * ``originatorDistance`` : The number of hops traveled from the originator.
    * ``target`` : A three-byte string representing the target for the routing packet.
    * ``targetDistance`` : A number representing the distance to the target.

Undecoded Packets
-----------------

.. attribute:: ``snap.RawDescriptor``

``RawDescriptor`` may show up in cases where a packet could not be decoded and broken into the correct components.  A
raw descriptor contains no additional information outside of the attributes common to all descriptors.

RPC Packets
-----------

.. attribute:: ``snap.RpcDescriptor``

``RpcDescriptor`` represents received and transmitted RPC packets.

See functions :meth:`~Snap.rpc()`, :meth:`~Snap.mcast_rpc()`, and :meth:`~Snap.dmcast_rpc()`.
    * ``args`` : A tuple of arguments to be passed to the RPC function.
    * ``dstAddr`` : A three-byte string representing the immediate destination of the packet (subject to mesh routing) or a two-byte multicast group (for a multicast packet).
    * ``final_dst_addr`` : A three-byte string representing the final destination of the packet (unicast only).
    * ``funcName`` : Name of the RPC function to be called.
    * ``isMulticast`` : True if the packet is multicast or False if it is unicast.
    * ``last_hop_addr`` : A three-byte string representing the immediate source of the packet.
    * ``seq`` : The sequence number of the packet.
    * ``srcAddr`` : A three-byte string representing the original source of the packet.
    * ``ttl`` : The number of hops remaining for this packet (multicast only).

Trace Route Packets
-------------------

.. :attribute:: ``snap.TraceRouteDescriptor``

``TraceRouteDescriptor`` represents received and transmitted traceroute packets.

See function :meth:`~Snap.traceroute()`. See :attr:`~snappy.hooks.HOOK_TRACEROUTE` for information on how traceroute packets are received.
    * ``dstAddr`` : A three-byte string representing the immediate destination of the packet.
    * ``elapsed`` : The elapsed time in milliseconds to reach the target node. (This time does not include the first hop in the path, which will typically be trivial for serial connections but can be significant when SNAP Connect performs a traceroute over a TCP bridge.)
    * ``final_dst_addr`` : A three-byte string representing the final destination of the packet.
    * ``isMulticast`` : True if the packet is multicast or False if it is unicast.
    * ``msgId`` : A single character representing the type of traceroute packet. ‘Q’ is used for traceroute queries and ‘P’ is used for traceroute replies.
    * ``orig_src_addr`` : A three-byte string representing the original source of the packet.
    * ``records`` : A list of traceroute records with ‘address’ and ‘linkQuality’ attributes.
    * ``srcAddr`` : A three-byte string representing the immediate source of the packet.
