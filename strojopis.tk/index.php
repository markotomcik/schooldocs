<?php
session_start();

require_once("functions.php");
start_page("Strojopis");
user();

require_once("templates/index.template.php");

end_page();