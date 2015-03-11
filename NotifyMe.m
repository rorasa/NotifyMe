function NotifyMe(service, command, varargin)

if nargin < 2
    error('Please supply input arguments');
end
args = varargin{1};
query = ['python notifyme.py ',service,' ',command,' "',args,'"'];
system(query);
