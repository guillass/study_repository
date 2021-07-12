from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/u2")
def hello_galado():
    return "<p>Hello, Galado!</p>"



@app.route("/tora")
def tora_reia():
    return """<!DOCTYPE html>

<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="tora_reia2.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">
    <title>Tora-reia no Roshan</title>

</head>

<body>
    <div id="principal">
        <div id="cabecalho">
            <h1>&nbsp;</h1>
            <img style="width:70%; height:70%;" src="https://torareianoroshan.github.io/podcast/imagens/logo.png">
            <img style="width:20%; height:20%;" src="https://torareianoroshan.github.io/podcast/imagens/roshpng01.png">
        </div>

        <div id="intro">
            <h4>Podcast dedicado ao contaditório joguinho de computador: DOTA2</h4>
        </div>

        <div class="podcasts">
            <h4>Ouça agora:</h4>
            <ul class="stream">
                <li>
                    <a href="https://open.spotify.com/show/2KNBoD6bcMHpsYNek1wiHQ" target="_blank" class="strm-spotfy" title="Spotfy">Spotfy</a>
                </li>
                <li>
                    <a href="https://radiopublic.com/torareia-no-roshan-6nJE3Y" target="_blank" title="Radio Public">Radio Public</a>
                </li>
                <li>
                    <a href="https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy81MzFiZmIyYy9wb2RjYXN0L3Jzcw==" target="_blank" title="Google Podcasts">Google Podcasts</a>
                </li>
                <li>
                    <a href="https://www.breaker.audio/tora-reia-no-roshan" target="_blank" title="Breaker">Breaker</a>
                </li>
            </ul>
        </div>

        <div id="episodios-logo">
            <img style="width: 200px; height: 200px;" src="imagens/epi.svg">
        </div>
        
        <!--- repetir essa div quando for adicionar novos episódios -->
        <!--- maximo de 2 episodios por div -->
        <div class="episodios">
            <div class="epi">
                <img src="https://torareianoroshan.github.io/podcast/imagens/epi1_cover.png" alt="Episódio 1">
                <a class="epi-txt-num" href="link_pagina">Episódio 1</a>
                <h4 class="epi-txt-desc" >Início da jornada dos nossos podcasters =(</h4>
            </div>
            
            <div class="epi">
                <img src="https://torareianoroshan.github.io/podcast/imagens/epi1_cover.png" alt="Episódio 1">
                <a class="epi-txt-num" href="link_pagina">Episódio 1</a>
                <h4 class="epi-txt-desc" >Início da jornada dos nossos podcasters =(</h4>
            </div>
            
        </div>
       
<!---
        <div class="episodios">
            <div class="epi">
                <img src="imagens/epi1_cover.png" alt="Episódio 1">
                <a class="epi-txt-num" href="link_pagina">Episódio 1</a>
                <h4 class="epi-txt-desc" >Início da jornada dos nossos podcasters =(</h4>
            </div>
            
            <div class="epi">
                <img src="imagens/epi1_cover.png" alt="Episódio 1">
                <a class="epi-txt-num" href="link_pagina">Episódio 1</a>
                <h4 class="epi-txt-desc" >Início da jornada dos nossos podcasters =(</h4>
            </div>
            
        </div>
-->
    </div>

</body> """