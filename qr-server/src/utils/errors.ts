export class generalError extends Error {
    message: string
    details: string
    constructor(msg: string = "", details = null) {
        super();
        this.message = msg || '';
        this.details = details || '';
    }

    getCode() {
        if (this instanceof Unauthorized) { return 403 }
        if (this instanceof Unauthenticated) { return 401 }
        if (this instanceof Internal) { return 500 }
        return 500;
    }
}

export class Unauthorized extends generalError {
    constructor() {
        super(); this.message = this.message ? this.message : 'Unauthorized to access this resource'
    }
}

export class Unauthenticated extends generalError {
    constructor() {
        super(); this.message = this.message ? this.message : 'You need to authenticate to access this resource'
    }
}

export class Internal extends generalError {
    constructor(error: string) {
        super(error);
        this.message = this.message ? this.message : 'Internal server error';
    }
}