<template>
  <div></div>
</template>

<script>
window.onload = function(){
    console.log("Oi")
    intialize();
}
function intialize() {
    const height = 10
    const width = 10
    // Create the game board
    for (let r = 0; r < height; r++) {
        for (let c = 0; c < width; c++) {
            // <span id="0-0" class="tile">P</span>
            let tile = document.createElement("div");
            tile.innerText = 'oi'
            tile.id = r.toString() + "-" + c.toString();
            tile.classList.add("tile");
            document.body.appendChild(tile)
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
.tile {
    /* Box */
    border: 2px solid lightgray;
    width: 60px;
    height: 60px;
    margin: 2.5px;

    /* Text */
    color: black;
    font-size: 36px;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
