import {Clip} from '../Models'

export class DataHandler {
    static async getClips() : Promise<Clip[] | string>  {
        const response = await fetch("/api/clips")

        switch (response.status) {
            case 200:
                return await response.json()
            case 404:
                return "Data not found"
            case 500:
                return "Internal server error"
            default:
                return await response.text()
        }
    }
}