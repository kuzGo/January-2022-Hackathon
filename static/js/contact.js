const btn = document.getElementById('contactButton');

        document.getElementById('form')
            .addEventListener('submit', function (event) {
                event.preventDefault();

                btn.value = 'Sending...';

                const serviceID = 'service_lym8jev';
                const templateID = 'template_xtu3dol';

                emailjs.sendForm(serviceID, templateID, this)
                    .then(() => {
                        btn.value = 'Subscribe';
                        swal({
                            title: "Message Sent!",
                            text: "Thank you for getting in touch!",
                            icon: "success",
                            button: "Ok,thanks!",
                        });
                        form.reset();
                    }, (err) => {
                        btn.value = 'Subscribe';
                        console.log(JSON.stringify(err));
                        swal("Apologies!", "Something went wrong!", "error");
                    });
            });