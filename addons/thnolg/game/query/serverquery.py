import datetime


class ServerQuerier:
    SERVER_WAIT_TIME = 1

    server_timers = {}

    def __init__(self):

        pass

    @staticmethod
    def _check_server(server=None):
        now = datetime.datetime.now()
        if server in ServerQuerier.server_timers:
            server_time = ServerQuerier.server_timers.get(server)
            if (now - server_time).total_seconds() > ServerQuerier.SERVER_WAIT_TIME:
                ServerQuerier.server_timers.pop(server)
                return True
            return False

        ServerQuerier.server_timers[server] = now
        return True

    @staticmethod
    def send_command(server=None, command=""):
        if server is None:
            return None

        if command is None or len(command) == 0:
            return None

        # while (!checkServer(server)) {
        #     try {
        #         Thread.sleep(SERVER_WAIT_TIME);
        #     } catch (InterruptedException e) {
        #         e.printStackTrace();
        #     }
        # }
        #
        # for (int i = 0; i < SERVER_MAX_ATTEMPT; i++) {
        #     logger.debug(String.format("Attempt %d on %s for \"%s\"", i, server.getTag(), command));
        #     if (i > 0) {
        #         try {
        #             Thread.sleep(1000);
        #         } catch (InterruptedException e) {
        #             e.printStackTrace();
        #         }
        #     }
        #     String cmd = String.format("rcon %s %s\n", server.getRconPassword(), command);
        #     byte[] data = new byte[4 + cmd.length()];
        #     data[0] = (byte) 0xFF;
        #     data[1] = (byte) 0xFF;
        #     data[2] = (byte) 0xFF;
        #     data[3] = (byte) 0xFF;
        #     System.arraycopy(cmd.getBytes(), 0, data, 4, cmd.length());
        #
        #     byte[] rawdata = null;
        #     try {
        #         DatagramSocket socket = new DatagramSocket();
        #         socket.setReceiveBufferSize(65535);
        #         socket.setSendBufferSize(65535);
        #         socket.setSoTimeout(2000);
        #         InetAddress address = InetAddress.getByName(server.getAddress());
        #         socket.connect(address, server.getPort());
        #
        #         DatagramPacket queryPacket = new DatagramPacket(data, data.length, address, server.getPort());
        #         socket.send(queryPacket);
        #
        #         Thread.sleep(500);
        #
        #         byte[] buffer = new byte[65535];
        #         DatagramPacket responsePacket = new DatagramPacket(buffer, buffer.length);
        #         socket.receive(responsePacket);
        #         rawdata = Arrays.copyOfRange(responsePacket.getData(), 4, responsePacket.getData().length);
        #
        #         socket.close();
        #     } catch (InterruptedException e) {
        #         logger.warn("Interrupted");
        #     } catch (SocketTimeoutException e) {
        #         logger.warn(String.format("Socket timeout for %s", server.getTag()));
        #     } catch (UnknownHostException e) {
        #         logger.error(String.format("Unknown host for %s", server.getAddress()));
        #     } catch (PortUnreachableException e) {
        #         logger.error(String.format("Port unreachable for %s:%d", server.getAddress(), server.getPort()));
        #     } catch (IOException e) {
        #         e.printStackTrace();
        #     }
        #
        #     if (rawdata == null) {
        #         continue;
        #     }
        #     String response = new String(rawdata).replaceAll("\u0000.*", "");
        #     if (response.length() == 0) {
        #         continue;
        #     }
        #     return response;
        # }

        return None
