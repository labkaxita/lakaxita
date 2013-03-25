({
    mainConfigFile: 'main.js',
    optimize: 'uglify',
    preserveLicenseComments: false,
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
