
document.getElementById('submit-button').addEventListener('click', PythonPipeline);
document.getElementById('random-genre-btn').addEventListener('click', PythonPipeline);

async function PythonPipeline(){

    const user_input = document.getElementById('user-input').value;
    
    const payload = {user : user_input}


    const user_input_json = JSON.stringify(payload);


    const response = await fetch('http://127.0.0.1:5000/generate_lit', {
        method: 'POST',
        body: user_input_json,
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const data = await response.json();
    document.getElementById('core-text').innerHTML = data.core;
    document.getElementById('character-text').innerHTML = data.character;
    document.getElementById('setting-text').innerHTML = data.setting;
    document.getElementById('plot-text').innerHTML = data.plot;

    document.getElementById('waiting-text').style.display = 'none';

    console.log(data);






}