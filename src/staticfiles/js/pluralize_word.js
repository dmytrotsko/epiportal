const isPlural = num => Math.abs(num) !== 1;
const simplePlural = word => `${word}s`;
const pluralize = (num, word, plural = simplePlural) =>
    isPlural(num) ? plural(word) : word;