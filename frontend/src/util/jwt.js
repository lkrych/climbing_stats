import  jwt  from 'jwt-decode';

export const getUserId = () => {
    const decoded = jwt(localStorage.getItem('jwt'));
    return decoded.identity.id;
}