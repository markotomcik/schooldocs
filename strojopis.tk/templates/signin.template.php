<?php
if (isset($_GET["error"]) && !empty($_GET["error"])) {
    if ($_GET["error"] == "user") {
        $error = "user";
    } else if ($_GET["error"] == "server") {
        $error = "server";
    } else {
        $error = "error";
    }
} else {
    $error = "";
}
?>

<form action="postdata.php?from=<?php echo urlencode("/signin.php"); ?>&to=<?php echo urlencode("/"); ?>&else=<?php echo urlencode("/signin.php?error="); ?>" method="POST">
    <h1>Prihlásenie</h1>
    <input type="hidden" name="id" value="">
    <input <?php if (!empty($error)) echo "class=\"error\""?> type="text" name="email" id="email" placeholder="E-mail">
    <input <?php if (!empty($error)) echo "class=\"error\""?> type="password" name="password" id="password" placeholder="Heslo">
    <?php if ($error == "user") echo "<div class=\"error\">Chybné meno alebo heslo!</div>" ?>
    <?php if ($error == "server") echo "<div class=\"error\">Chyba na strane servera.<br><br>KONTAKTUJTE ADMINA!<br><a class=\"error\" href=\"mailto:markotomcik@gmail.com\">markotomcik@gmail.com</a></div>" ?>
    <?php if ($error == "error") echo "<div class=\"error\">Neznáma chyba.<br><br>KONTAKTUJTE ADMINA!<br><a class=\"error\" href=\"mailto:markotomcik@gmail.com\">markotomcik@gmail.com</a></div>" ?>
    <input type="submit" value="Prihlásiť">
    <h1>Užitočné linky</h1>
    <ul>
        <li><a href="https://forms.gle/4Fis4XzpiJXNiqP19">Formulár na odovzdanie</a></li>
        <li><a href="https://typingclub.com/strojopis">typingclub.com</a></li>
        <li><a href="https://zty.pe">zty.pe</a></li>
    </ul>
</form>