<header>
    <div>Ste prihlásený ako <?php echo $_SESSION[USER][NAME] . " " . $_SESSION[USER][SURNAME]; ?></div>
    <a href="/logout.php">Odhlásiť sa</a>
</header>

<div>
    <aside>
        <nav>
            <ul>
                <li><input id="ko" type="checkbox" name="ko">
                    <label for="ko">Kontrolný opis</label>
                    <ul>
                        <li><a href="#">Nový</a></li>
                        <li><a href="#">Záznamy</a></li>
                    </ul>
                </li>
                <li><a href="#">Domáca úloha</a>
                    <ul>
                        <li><a href="#">Nový</a></li>
                        <li><a href="#">Záznamy</a></li>
                    </ul>
                </li>
                <li><a href="#">Precvičovanie</a></li>
                <li><a href="#">Môj profil</a></li>
            </ul>
        </nav>
    </aside>

    <main>
        <h1>Kontrolný opis</h1>
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quas quidem dicta omnis, hic porro quisquam adipisci animi harum architecto reprehenderit nobis error cum sunt quod doloremque! Impedit autem corrupti deleniti.</p>
    </main>
</div>