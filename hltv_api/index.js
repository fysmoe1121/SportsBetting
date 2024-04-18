const { HLTV }  = require('hltv'); // Replace 'hltv-api' with the actual name of the module

console.log(HLTV); // This will print out the HLTV object to see if getMatches is a method

//HLTV.getTeamByName({name: "FaZe"}).then(res => {
//   console.log(res)
//})

//HLTV.getTeamStats({id: 6667} ).then((res) => {
//  console.log(res)
//})

HLTV.getPlayerStats({id: 11816}).then((res) => {
    console.log(res["overviewStatistics"])
})