<?php
session_start();

require_once("functions.php");
start_page("Prihlásenie");

require_once("templates/signin.template.php");

end_page();