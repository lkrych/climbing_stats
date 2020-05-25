import styled from 'styled-components';

export const Button = styled.button`
    border-radius: 2px;
    border: 2px solid #f9cd0e;
    background-color: Transparent;
    font-size: 1.25rem;
    color: #f9cd0e;
    padding: 1rem 2rem;
    margin: 0 auto;
    cursor: pointer;
    transition: font-size .5s linear;
    -o-transition: font-size .25s linear; 
    -moz-transition: font-size .25s linear; 
    -webkit-transition: font-size .25s linear; 

    &:hover {
        background: white;
    }

    @media (max-width: 600px) {
        font-size: 1rem;
        padding: .75rem 1.75rem;
    }
`

export const MainHeader = styled.h1`
    font-size: 6rem;
    font-weight: normal;
    margin-bottom: 0;
    color: #f9cd0e;
`

export const SubHeader = styled.h2`
    font-size: 3rem;
    font-weight: normal;
    color: white;
`

export const Text = styled.p`
    font-size: 2rem;
    font-weight: normal;
    color: white;
`

export const CharCount = styled.p`
    font-size: 0.9rem;
    margin: 0.5rem;
    color: ${props => props.exceedChars ? "red" : "black"} 
`