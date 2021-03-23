import variable as v;
import character.group2.yashiro.text as t;
import func.sound as s;

var prevValue = 0;
var stack = 0;

function text(playerID);

function main(playerID)
{
   if (v.P_KillScore[playerID] != prevValue)
   {
      var killPoint = v.P_KillScore[playerID] - prevValue;
      
      stack += killPoint;
      prevValue = v.P_KillScore[playerID];
      
      SetDeaths(playerID, Add, killPoint, " `UniqueSkill");
   }
   text(playerID);
}

function text(playerID)
{
   if (stack > 0)
   {
      var uniqueCount = dwread_epd(204 * 12 + playerID);
      var isAllCleared = 1;      //TRUE
      for (var i = 0; i < 6; i++) 
      {
         if (t.P_TextTime[i] > 0) { isAllCleared = 0; }
      }
      if (isAllCleared == 1)
      {
         s.CharacterVoice(1000 + uniqueCount % 8);
      }
      stack -= 1;
   }
}