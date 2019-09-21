d3.csv("/../social-power-nba/nba_2017_salary.csv", function(data, error) {
    var data1 = data
    console.log(data);
    return data1;
  
  var dataset = [];
  function handleClick(event){
    console.log(document.getElementById("myVal").value)
    draw(document.getElementById("myVal").value)
    return false;
};
function draw(val){
    d3.select("body").select("ul").append("li");
    dataset.push(val);
    var p = d3.select("body").selectAll("li")
    .data(dataset)
    .text(function(d,i){return i + ": " + d;})
};
});