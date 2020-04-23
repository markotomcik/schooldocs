<?php
# Načíta konfiguračné súbory
function load_config()
{
    require_once("config/define.config.php");
    require_once("config/main.config.php");
}

# Zistí či je užívateľ prihlásený
function user_exist()
{
    if (isset($_SESSION[USER][LOGGEDIN]) && !empty($_SESSION[USER][LOGGEDIN]) && $_SESSION[USER][LOGGEDIN]) {
        return true;
    } else {
        return false;
    }
}

# Presmeruje neprihláseného užívateľa na stránku signin.php
function user()
{
    if (!user_exist()) {
        header("Location: /signin.php");
        exit;
    }
}

# Rutina na začiatku každej stránky
function start_page($title)
{
    load_config();
    set_title("ADK | " . $title);
    require_once("templates/head.template.php");
}

function end_page()
{
    require_once("templates/foot.template.php");
}

# Nastaví title stránky
function set_title($title)
{
    $_SESSION[TITLE] = $title;
}

# Vráti title stránky
function get_title()
{
    return $_SESSION[TITLE];
}

function get_page()
{
    return basename($_SERVER['PHP_SELF'], ".php");
}