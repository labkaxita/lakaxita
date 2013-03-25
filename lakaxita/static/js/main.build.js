({
    mainConfigFile: 'main.js',
    optimize: 'uglify',
    removeCombined: true,
    modules: [
        {
            name: 'backbone-tastypie',
            include: ['backbone'],
        },
        {
            name: 'lakaxita/app',
        },
    ],
})
