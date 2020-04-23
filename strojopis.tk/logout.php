<?php
session_start();

require_once("functions.php");
start_page("Log out");

session_destroy();

header("Location: /signin.php");
exit();