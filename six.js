// Run with node js
var fs = require("fs"),
path = require("path");

var dir_name = "/media/d4insight/backup/sample/"

function depthfirstsearch(dir_name, visited = [], results = []){
    fs.readdir(dir_name, (err, files) => {
      files.forEach(file => {
        new_dir = dir_name + file + '/';
        // console.log(new_dir)
        if (fs.existsSync(new_dir) && visited.indexOf(new_dir) == -1){
            visited.push(new_dir)
            results.push(new_dir)
            console.log(new_dir)
            depthfirstsearch(new_dir, visited, results)
        }
        else{
            results.push(dir_name+file)
            console.log(dir_name+file)
        }
      });
    })


}
depthfirstsearch(dir_name)
