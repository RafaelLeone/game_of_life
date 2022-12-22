<template>
  <div></div>
</template>

<script>
window.onload = function(){
  inicializa();
}
async function inicializa() {
  const altura = 10
  const largura = 10
  // Cria o tabuleiro:
  for (let linha = 0; linha < altura; linha++) {
    for (let coluna = 0; coluna < largura; coluna++) {
      let quadrado = document.createElement("div");
      quadrado.innerText = ''
      quadrado.id = linha.toString() + "-" + coluna.toString();
      quadrado.classList.add("quadrado");
      document.body.appendChild(quadrado)
    }
  }
  // Padrão inicial:
  let quadradoVivoInicial1 = document.getElementById("1-2")
  quadradoVivoInicial1.classList.add("quadradoAmarelo")
  let quadradoVivoInicial2 = document.getElementById("2-3")
  quadradoVivoInicial2.classList.add("quadradoAmarelo")
  let quadradoVivoInicial3 = document.getElementById("3-1")
  quadradoVivoInicial3.classList.add("quadradoAmarelo")
  let quadradoVivoInicial4 = document.getElementById("3-2")
  quadradoVivoInicial4.classList.add("quadradoAmarelo")
  let quadradoVivoInicial5 = document.getElementById("3-3")
  quadradoVivoInicial5.classList.add("quadradoAmarelo")

  for (let linha = 0; linha < altura; linha++) {
    for (let coluna = 0; coluna < largura; coluna++) {
      let quadradoAtual = document.getElementById(`${linha.toString()}-${coluna.toString()}`)
      const promise = new Promise((resolve) => {
        setTimeout(() => {
          resolve(checaQuadrado(quadradoAtual));
        }, 1000)
      })
      await promise.then(response => {
      console.log(response);
    })
  }
}

function checaQuadrado(quadradoAtual) {
  quadradoAtual.innerText = 'Oi'
  return
}

  // setTimeout(() => {
  //   let quadradoVivoInicial1 = document.getElementById("1-2")
  //   quadradoVivoInicial1.classList.remove("quadradoAmarelo")
  //   let quadradoVivoInicial3 = document.getElementById("3-1")
  //   quadradoVivoInicial3.classList.remove("quadradoAmarelo")
  //   let quadradoVivoInicial2 = document.getElementById("2-1")
  //   quadradoVivoInicial2.classList.add("quadradoAmarelo")
  //   let quadradoVivoInicial4 = document.getElementById("4-2")
  //   quadradoVivoInicial4.classList.add("quadradoAmarelo")
  // }, 3000);
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
  background-color: white;
  border: 2px solid lightgray;
  width: 55px;
  height: 55px;
  margin: 2.5px;

  /* Texto */
  color: black;
  font-size: 36px;
  font-weight: bold;
  display: flex;
  justify-content: center;
  align-items: center;
}
.quadradoAmarelo {
  background-color: yellow;
}
</style>
