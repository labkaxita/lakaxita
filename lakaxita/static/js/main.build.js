({
    mainConfigFile: 'main.js',
    optimize: 'uglify',
    preserveLicenseComments: false,
    removeCombined: true,
    modules: [
        {
            name: 'main',
            include: ['backbone'],
        },
    ],
})
