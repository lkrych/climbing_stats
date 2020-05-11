const API_HOST = process.env.API_HOST

const buildUrl = (route, paramsObj = {}) => {
    let url = `http://${API_HOST}${route}`;
    let params = Object.keys(paramsObj);
    if (params.length > 0) {
        url += '?'
        let queryString = params.map(key => key + '=' + paramsObj[key]).join('&');
        url += queryString
    }
    return url;
}

export const getRequest = (route, params = {}) => {
    let url = buildUrl(route, params);
    return fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
            'Content-Type': 'application/json',
        }
    })
    .then(handleResponse)
    .then(json => json)
}

export const postRequest = (route, data) => {
    let url = buildUrl(route);
    return fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
            'Content-Type': 'application/json',
          },
    })
    .then(handleResponse)
    .then(json => json)
}

const handleResponse = (response) => {
    return response.json()
        .then(json => Object.assign({}, json, { 'status_code': response.status }))
}