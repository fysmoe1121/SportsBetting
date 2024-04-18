const { HLTV }  = require('hltv'); // Replace 'hltv-api' with the actual name of the module

console.log(HLTV); // This will print out the HLTV object to see if getMatches is a method

HLTV.getMatch({ id: 2306295 }).then(res => {
    console.log(res)
})
