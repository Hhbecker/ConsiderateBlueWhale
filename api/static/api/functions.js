

function deleteFile(id) {
    fetch('/api/list/delete/' + id, {method: 'DELETE'});
    //location.href = '/api/list/';
    location.reload(true);
}

function goToUpdateFile(id) {
    console.log("Inside gotToUpdateFile function");
    // fetch('/api/list/update/' + id, {method: 'GET'});
    location.href = '/api/list/update/' + id, {method: 'GET'};
}

var isPlaying = false;
function playSong(url){
    const music = new Audio(url);
    console.log("Inside playSong function");
    console.log(url);

    if(isPlaying==false){
        isPlaying==true;
        music.play();
    }
    else{
        isPlaying==false;
        music.pause();
    }
    
}