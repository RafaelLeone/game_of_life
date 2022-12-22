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
      // let quadradoAtual = document.getElementById(`${linha.toString()}-${coluna.toString()}`) // Era teste
      const promise = new Promise((resolve) => {
        setTimeout(() => {
          resolve(checaQuadrado(linha, coluna))
        }, 1000)
      })
      await promise.then(response => {
      console.log(response)
    })
  }
}

function checaQuadrado(linha, coluna) {
  let vizinhos = []
  let numero_de_vizinhos_vivos = 0
  vizinhos.push(document.getElementById(`${(linha-1).toString()}-${(coluna-1).toString()}`)) // N esquerda
  vizinhos.push(document.getElementById(`${(linha-1).toString()}-${(coluna-0).toString()}`)) // N
  vizinhos.push(document.getElementById(`${(linha-1).toString()}-${(coluna+1).toString()}`)) // N direita
  vizinhos.push(document.getElementById(`${(linha-0).toString()}-${(coluna-1).toString()}`)) // Esquerda
  vizinhos.push(document.getElementById(`${(linha-1).toString()}-${(coluna+1).toString()}`)) // Direita
  vizinhos.push(document.getElementById(`${(linha+1).toString()}-${(coluna-1).toString()}`)) // S esquerda
  vizinhos.push(document.getElementById(`${(linha+1).toString()}-${(coluna-0).toString()}`)) // S
  vizinhos.push(document.getElementById(`${(linha+1).toString()}-${(coluna+1).toString()}`)) // S direita
  // quadradoAtual.innerText = 'Oi' // Era teste
  for (let vizinho of vizinhos) {
    /* eslint-disable no-debugger */
    // debugger
    /* eslint-enable no-debugger */
    if (vizinho != null) {
      if (vizinho.className === 'quadrado quadradoAmarelo'){
        numero_de_vizinhos_vivos++
      }
    }
    // if (vizinho.classList === "quadrado quadradoAmarelo") {
    //   numero_de_vizinhos_vivos ++
    // }
  }
  console.log(numero_de_vizinhos_vivos)
  return
}
  // Esperado do tempo seguinte:
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
