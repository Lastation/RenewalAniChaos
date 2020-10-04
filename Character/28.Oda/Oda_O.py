import Function as f;

const posX = PVariable();

const posY = PVariable();

var max_n = 5;

function savePosRoutine(cp)
{
   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");

   for (var i = 5; i > 0; i--)
   {
      posX[i] = posX[i - 1];
      posY[i] = posY[i - 1];
   }
   
   const location = EPD(0x58DC4C) + f.location[cp] * 5;

   posX[0] = dwread_epd(location + 2);
   posY[0] = dwread_epd(location + 1);
}

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("Recall - Oda", Set);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }

         if (f.loop[cp] == 1)
         {
             setloc(f.location[cp], posX[max_n], posY[max_n]);
               MoveUnit(All, f.heroID[cp], cp, "Anywhere", f.location[cp]);
               CenterView(f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 2)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         SetSwitch("Recall - Oda", Clear);
         SetDeaths(cp, SetTo, 2160, " `UniqueCoolTime");
         f.SkillEnd(cp);
      }
   }
   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");

}