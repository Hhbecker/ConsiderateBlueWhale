

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

function playSong(url){
    console.log("Inside playSong function");
    console.log(url);
    const music = new Audio(url);
    music.play();
}