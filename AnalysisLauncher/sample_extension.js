

getCurrentUrl = () => {

    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){

        let xhr = new XMLHttpRequest();
        xhr.open("POST", `http://localhost:5000/getAnalysis`);
        xhr.setRequestHeader('Content-Type', 'application/json');
        const data = { "url" : tabs[0].url.toString() }
        xhr.send(JSON.stringify(data));
        xhr.onload = () => {
            if(xhr.status === 200){
                const message = JSON.parse(xhr.response)
                document.querySelector("#msg").innerText = message.response
            }
            else{
                console.log(`error ${xhr.status}`)
            }
        }
    });

}

document.getElementById("myButton").addEventListener("click", getCurrentUrl);