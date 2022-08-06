<?php

    // Constants
    define("MSG_SIZE", 1024);
    define("MSG_SIZE_LARGE", 8192);
    define("SOCK_PATH", "/home/ubuntu/Documents/GitHub/daemons/testing.sock");

    /* Create a Connection to Socket */
    function unix_socket(string $path) {
        $socket = socket_create(AF_UNIX, SOCK_STREAM, 0);
        if (!$socket) return false;
        if (!socket_connect($socket, $path)) return false;
        return $socket;
    }

    /* Send Command to Stream */ 
    function send_command(Socket $socket, string $command) {
        return socket_write($socket, $command."\0", MSG_SIZE);
    }

    /* Read Server Response */
    function read_response(Socket $socket, string $command) {
        $buffer = socket_read($socket, MSG_SIZE_LARGE);
        if (!$buffer) return false;
        return explode("\0", $buffer)[0];
    }

    // Open Connection
    $socket = unix_socket(SOCK_PATH);

    // Send Commands
    if ($socket) {
        send_command($socket, "add symbol 1 BTC_USDT");
        send_command($socket, "add book 1");
        send_command($socket, "add limit sell 1 1 20000 1");
        echo(read_response($socket, "get book 1")."\n");
        send_command($socket, "add limit buy 1 1 20000 1");
        echo(read_response($socket, "get book 1")."\n");

        // Close Connection
        socket_close($socket);
    }
    
?>
