/** @type {import('./$types').Actions} */
export const actions = {
    default: async ({request}) => {
        console.log("submitted")
        const data = await request.formData();
        const username = data.get('email');
        const password = data.get('password');
        let result = await fetch("http://127.0.0.1:5000/login",
            {
                method:"POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body:JSON.stringify({
                    username:username,
                    password:password
                })
            } 
        )
        if (result.ok){
            return {
                token:await result.text()
            }
        }
    }
  };