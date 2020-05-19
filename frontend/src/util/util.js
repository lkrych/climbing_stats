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
