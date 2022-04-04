const mongoose = require('mongoose')
const Schema = mongoose.Schema // defines the schema of the data

// schema
const librarySchema = new Schema({
    rows: {
        type: Number,
        required: true
    },
    columns: {
        type: Number,
        required: true
    }
}, { timestamps: true });

// model. The string defines the model name (very important)
const Library = mongoose.model('Library', librarySchema)
module.exports = Library