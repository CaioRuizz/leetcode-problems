function findChampion(grid: number[][]): number {
    const victories = grid.map(team => team.reduce((x, y) => x + y));
    return victories.indexOf(victories.reduce((x, y) => Math.max(x, y)));
};