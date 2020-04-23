<?php
session_start();

require_once("functions.php");
start_page("POST data");

if ($_GET["from"] == "/signin.php") {
    $mysqli = new mysqli($_SESSION[MYSQLI_HOST], $_SESSION[MYSQLI_USER], $_SESSION[MYSQLI_PASS], $_SESSION[MYSQLI_DB]);

    if ($mysqli->connect_errno) {
        header("Location: " . $_GET["else"] . "server");
        exit();
    }

    if ($result = $mysqli->query("SELECT * FROM users WHERE email=\"" .  $_POST["email"] . "\"")) {
        if ($row = $result->fetch_assoc()) {
            if ($row["password"] == md5($_POST["password"])) {
                $_SESSION[USER][LOGGEDIN] = true;
                $_SESSION[USER][ID] = $row[ID];
                $_SESSION[USER][EMAIL] = $row[EMAIL];
                $_SESSION[USER][NAME] = $row[NAME];
                $_SESSION[USER][SURNAME] = $row[SURNAME];
                $_SESSION[USER][AUTH] = $row[AUTH];
                $_SESSION[USER][SIGNUP] = $row[SIGNUP];
                $_SESSION[USER][LASTSIGNIN] = $row[LASTSIGNIN];

                $result->close();

                if (!$mysqli->query("UPDATE users SET lastsignin=CURRENT_TIMESTAMP WHERE id=" . $_SESSION[USER][ID])) {
                    header("Location: " . $_GET["else"] . "server");
                }

                header("Location: " . $_GET["to"]);
            } else {
                header("Location: " . $_GET["else"] . "user");
            }
        } else {
            header("Location: " . $_GET["else"] . "user");
        }
    } else {
        header("Location: " . $_GET["else"] . "server");
    }

    $mysqli->close();
    exit();
}
end_page();
