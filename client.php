<?php

    // Constants
    define("MSG_SIZE", 1024);
    define("MSG_SIZE_LARGE", 8192);
    define("SOCK_PATH", "/home/ubuntu/GitHub/CppTrader/bin/daemons/test.sock");

    // Create a Connection to Given Socket
    function create_conn(string $path) {
        $socket = socket_create(AF_UNIX, SOCK_STREAM, 0);
        if (!$socket) return false;
        if (!socket_connect($socket, $path)) return false;
        return $socket;
    }

    function send_command(Socket $socket, string $command) {
        return socket_write($socket, $command."\n", MSG_SIZE);
    }

    function read_response(Socket $socket, string $command) {
        return socket_read($socket, MSG_SIZE_LARGE);
    }

    // Do commands
    $conn = create_conn(SOCK_PATH);
    if ($conn) {
        send_command($conn, "add symbol 1 BTC_USDT");
        send_command($conn, "add book 1");
        send_command($conn, "add limit sell 1 1 20000 1");
        echo(read_response($conn, "get book 1"));
        send_command($conn, "add limit buy 1 1 20000 1");
        echo(read_response($conn, "get book 1"));
        socket_close($conn);
    }
    
?>
