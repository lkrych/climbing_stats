const API_HOST = process.env.API_HOST

export const getRequest = (route) => {
    fetch(`http://${API_HOST}${route}`, {
        headers: {
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
        }
    })
    .then((response) => {
        return response.json();
    })
}

export const postRequest = (route, data) => {
    const url = `http://${API_HOST}${route}`
    console.log(`posting to ${url} with ${JSON.stringify(data)}`)
   return fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
            'Content-Type': 'application/json',

          },
    }).then((response) => {
            return response.json();
    })
}