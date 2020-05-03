// https://stackoverflow.com/a/10050831
export const range = (size, startAt = 0) => {
    return [...Array(size).keys()].map(i => i + startAt);
}