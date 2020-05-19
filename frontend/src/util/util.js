// https://stackoverflow.com/a/10050831
export const range = (size, startAt = 0) => {
    return [...Array(size).keys()].map(i => {
        return i + startAt
    });
}

export const rangeWithChars = (size, startAt = 0, chars) => {
    let gradedClimbs = [];
    let gradeRange = range(size, startAt);
    gradeRange.forEach(grade => {
        chars.forEach(char => {
            gradedClimbs.push(`${grade}${char}`)
        });
    })
    return gradedClimbs;
}

export const explodeClimbsObject = (obj, type) => {
    let objArray = [];
    Object.keys(obj).forEach(key => {
        objArray.push({
            grade: key,
            value: obj[key]
        });
    });
    if (type == "boulder") {
        objArray.sort((a, b) => parseInt(a['grade'].substring(1)) - parseInt(b['grade'].substring(1)));
    } else {
        objArray.sort((a, b) => {
            if (a.length < 2 && b.length < 2) {
                return parseInt(a) - parseInt(b);
            } else if (a.length < 2) {
                return -1
            } else if (b.length < 2) {
                return 1
            } else {
                let aGrade = parseInt(a['grade'].substring(0,2));
                let bGrade = parseInt(b['grade'].substring(0,2));
                if (aGrade == bGrade) {
                    a['grade'].charCodeAt(0) - b['grade'].charCodeAt(0);
                } else {
                    return aGrade - bGrade
                }
            }
        })
    }
    return objArray;
}

export const colorHash = {
    "0": "#6096BA",
    "1": "#5A92B7",
    "2": "#538DB5",
    "3": "#4D89B2",
    "4": "#4784B0",
    "5": "#4080AD",
    "6": "#3A7BAB",
    "7": "#3377A8",
    "8": "#2D72A6",
    "9": "#276EA3",
    "10a": "#276EA3",
    "10b": "#246A9B",
    "10c": "#226592",
    "10d": "#1F618A",
    "11a": "#1C5D81",
    "11b": "#195879",
    "11c": "#175470",
    "11d": "#144F68",
    "12a": "#114B5F",
    "12b": "#194C60",
    "12c": "#204D61",
    "12d": "#284D62",
    "13a": "#304E63",
    "13b": "#374F63",
    "13c": "#3F5064",
    "13d": "#465065",
    "14a": "#4E5166",
    "14b": "#4B4D60",
    "14c": "#48485A",
    "14d": "#444454",
    "15a": "#41404F",
    "15b": "#3E3B49",
    "15c": "#3B3743",
    "15d": "#37323D",
    "V0": "#FCBF49",
    "V1": "#FAB03D",
    "V2": "#F9A031",
    "V3": "#F79126",
    "V4": "#F5811A",
    "V5": "#F4720E",
    "V6": "#f26202",
    "V7": "#EC560A",
    "V8": "#E74B11",
    "V9": "#E13F19",
    "V10": "#DC3420",
    "V11": "#D62828",
    "V12": "#BD2020",
    "V13": "#A41818",
    "V14": "#8C1011",
    "V15": "#730809",
    "V16": "#5A0001"
}