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