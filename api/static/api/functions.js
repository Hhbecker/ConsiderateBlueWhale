

function deleteFile(id) {
    fetch('/api/list/delete/' + id, {method: 'DELETE'});
    fetch('/api/list/', {method: 'GET'});
}

function goToUpdateFile(id) {
    console.log("Inside gotToUpdateFile function")
    fetch('/api/list/update/' + id, {method: 'GET'});
}