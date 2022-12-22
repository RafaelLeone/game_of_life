<template>
  <div></div>
</template>

<script>
window.onload = function(){
    inicializa();
}
function inicializa() {
    const altura = 10
    const largura = 10
    // Create the game board
    for (let linha = 0; linha < altura; linha++) {
        for (let coluna = 0; coluna < largura; coluna++) {
            // <span id="0-0" class="tile">P</span>
            let quadrado = document.createElement("div");
            quadrado.innerText = 'oi'
            quadrado.id = linha.toString() + "-" + coluna.toString();
            quadrado.classList.add("quadrado");
            document.body.appendChild(quadrado)
        }
    }
}
</script>

<style>
body {
  width: 700px;
  height: 380px;
  margin: 0 auto;
  margin-top: 3px;
  display: flex;
  flex-wrap: wrap;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.quadrado {
    /* Quadrado */
    border: 2px solid lightgray;
    width: 60px;
    height: 60px;
    margin: 2.5px;

    /* Texto */
    color: black;
    font-size: 36px;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
