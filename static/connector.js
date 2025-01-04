
document.getElementById('submit-button').addEventListener('click', PythonPipeline);
document.getElementById('random-genre-btn').addEventListener('click', PythonPipeline);

async function PythonPipeline(){

    const user_input = document.getElementById('user-input').value;
    
    const payload = {user : user_input}


    const user_input_json = JSON.stringify(payload);


    try {
        const response = await fetch('http://192.168.18.9:5000/generate_lit', {
            method: 'POST',
            body: user_input_json,
            headers: {
                'Content-Type': 'application/json'
            }
        });
    
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
    
        const data = await response.json();
        document.getElementById('core-text').innerHTML = data.core;
        document.getElementById('character-text').innerHTML = data.character;
        document.getElementById('setting-text').innerHTML = data.setting;
        document.getElementById('plot-text').innerHTML = data.plot;
    
        document.getElementById('waiting-text').style.display = 'none';
        console.log(data);
    
    } catch (error) {
        console.error('Fetch error:', error);
        
    }
    





}