const { generalError } = require("../utils/errors")

const errorHandler = (err: any, req: any, res: any, next: any) => {
    if (err instanceof generalError) {
        res.status(err.getCode()).send({
            status: 'error',
            message: err.message,
        })
    }

    //solo por ahora
    res.status(500).send({
        status: 'error',
        message: err.message,
        details: 'internal server error'
    })
}

export default errorHandler;