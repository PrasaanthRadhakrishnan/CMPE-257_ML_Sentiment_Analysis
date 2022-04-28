
console.log("popup js ");

//chrome.action.onClicked.addListener(()=> { 
    console.log("clicked"); 
    chrome.tabs.query({active: true, currentWindow: true}, 
        function(tabs) {
        // since only one tab should be active and in the current window at once
        // the return variable should only have one entry
        let url = tabs[0].url;
        console.log(url)
        console.log(tabs[0].id)


     });
//});


