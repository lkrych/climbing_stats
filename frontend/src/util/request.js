const API_HOST = process.env.API_HOST

export const getRequest = (route) => {
    fetch(`http://${API_HOST}${route}`)
        .then((response) => {
            return response.json();
        })
}

export const postRequest = (route, data) => {
    const url = `http://${API_HOST}${route}`
    console.log(`posting to ${url} with ${JSON.stringify(data)}`)
    fetch(url, {
        method: 'POST',
        // mode: 'no-cors', // don't do this in production ;)
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          },
    })
        .then((response) => {
            return response.json();
        })
}