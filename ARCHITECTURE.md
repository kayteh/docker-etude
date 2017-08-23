## High level architecture

### WIP

This is currently a WIP but it is an effort to document the moving parts and
eventually document the public pluggable API that you can attach your services
to.


## DockerEtude

Composition
  parent class

  The entire glob/etude work is actually being defined and merged into a single
  composition


Service
  Single unit of work.
  It is defined the same way as a single docker container is defined in
  docker-compose

  Env
  Image
  Container
  Entrypoint
  Volumes


Composition `add_service(service)`

compostion.services => [service1, service2, service3]

Validation
  Services can have multiple validation
  Each validation can validate one thing

  For example: Validate that a file exists on the disk prior to bootstrapping
  the service or check that an environment variable exists and so on


validation = Validation.from_dict(JSON)

Loop through all of the validations that match the service
validation.validate(service)


