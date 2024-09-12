document.getElementById('form').addEventListener('submit',
    function(event){
        const input = document.getElementById('inbox').value;
        document.getElementById('given_input').innerHTML = "input:"+input;
        const url = 'https://mvnb9k0zac.execute-api.us-east-1.amazonaws.com/prod/invokemodel'
        fetch(url+"?"+encodeURIComponent(input),
            {
                method:'POST',
                headers: {'Content-Type':'application/json'}
            }
        )
        .then(response => response.json())
        .then(data =>
            {
                // console.log(data);
                document.getElementById('output').innerHTML = "output:"+data;
            }
        )
        event.preventDefault();
    }
)